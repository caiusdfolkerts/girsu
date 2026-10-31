import csv, importlib.util, io, json, os, sys, unittest
from pathlib import Path
HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parent));from query_examples import query,write_rows
ROOT=Path(os.environ.get('GIRSU_ROOT', HERE.parent))
READER=Path(os.environ.get('GIRSU_READER', ROOT/'girsu.py'))
spec=importlib.util.spec_from_file_location('released_girsu',READER)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Queries(unittest.TestCase):
 def setUp(self): self.g=m.Graph(ROOT)
 def rows(self,mode,text,sid='P100144'): return list(query(self.g,mode,text,[sid]))
 def test_null_genre(self):
  r=self.rows('genre','null')[0];self.assertIsNone(r['value']);self.assertEqual([q['id'] for q in r['qualifications']],['q5']);self.assertEqual(r['qualifications'][0]['null_reason'],'unresolved');self.assertFalse(r['has_branches']);self.assertTrue(r['has_ambiguity']);self.assertEqual(r['qualifications'][0]['reasoning_pointer'],'/reasoning/4')
 def test_date_applicability(self):
  r=self.rows('date','suen')[0];self.assertEqual(r['value']['kind'],'calendar');self.assertEqual(r['context']['date_applicability'][0]['value']['role'],'document_date');self.assertEqual(r['evidence'][0]['anchor']['id'],'ev17')
 def test_institution(self):
  r=self.rows('institution','szabra')[0];self.assertEqual(r['local_id'],'m2');self.assertFalse(r['has_branches']);self.assertTrue(r['has_ambiguity']);self.assertEqual(r['qualifications'][0]['id'],'q2')
 def test_commodity_with_quantity(self):
  r=self.rows('commodity','barley')[0];a=r['context']['measurements'][0]['value']['adopted'];self.assertEqual(a['components'],{'barig':'4','gur':'3'});self.assertEqual(a['standard_ref'],'gur_lugal');self.assertEqual(r['context']['qualifications_by_pointer']['/entries/0/measurements/0'][0]['id'],'q6')
 def test_relation_endpoints(self):
  r=self.rows('relation','metrological_standard')[0];self.assertEqual(r['local_id'],'relation2');self.assertEqual(r['context']['endpoints'][0]['local_id'],'entry1');self.assertEqual(r['qualifications'][0]['id'],'q6')
 def test_name_dedup_occurrences(self):
  rs=self.rows('person','ur-{d}nin-a-zu');self.assertEqual([r['local_id'] for r in rs],['m5','m7']);self.assertTrue(all(r['context']['count_unit']=='mention_occurrence_not_historical_entity' for r in rs))
 def test_exact_rational_and_csv_roundtrip(self):
  r=self.rows('commodity','', 'P100151');self.assertTrue(any('"1/2"' in json.dumps(v) for v in r));s=io.StringIO();write_rows(r,s,'csv');s.seek(0);back=[{k:json.loads(v) for k,v in row.items()} for row in csv.DictReader(s)];self.assertEqual(back,r)
 def test_jsonl_bindings(self):
  r=self.rows('genre','null');s=io.StringIO();write_rows(r,s);self.assertEqual([json.loads(x) for x in s.getvalue().splitlines()],r);self.assertEqual(r[0]['version_hash'],self.g.record_envelope('P100144')['version_hash']);self.assertEqual(r[0]['layer'],'source_preferred_research_default')
 def test_archival_explicit(self):
  with self.assertRaises(KeyError):list(query(self.g,'genre','letter',['P110939']))
  r=list(query(self.g,'genre','letter',['P110939'],True));self.assertEqual(len(r),1);self.assertFalse(r[0]['current'])
 def test_held_null_not_raw_fallback(self):
  real=self.g.research
  def held(sid,current_only=True):
   result=real(sid,current_only)
   result['record']['mentions'][1]['search_form']=None
   result['branches']=[{'status':'held','qualification_id':'q2','targets':['/mentions/1/search_form'],'null_cause':'unranked','is_identified_branch':True,'annotation_kind':'branch'}]
   return result
  self.g.research=held
  r=self.rows('institution','szabra')[0];self.assertIsNone(r['value']['search_form']);self.assertTrue(r['has_branches']);self.assertTrue(r['has_ambiguity']);self.assertEqual(r['branches'][0]['null_cause'],'unranked')
if __name__=='__main__':unittest.main()
