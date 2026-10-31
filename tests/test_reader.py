"""Portable reader regressions; standard library, no builder/source database."""
import hashlib,importlib.util,json,os,subprocess,sys,unittest
from pathlib import Path
ROOT=Path(os.environ.get('GIRSU_ROOT',Path(__file__).resolve().parents[1]))
READER=Path(os.environ.get('GIRSU_READER',ROOT/'girsu.py'))
spec=importlib.util.spec_from_file_location('released_girsu',READER)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Reader(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.g=m.Graph(ROOT)
 def test_single_default_hash(self):
  r=self.g.research('P102673');self.assertNotIn('canonical_value',r)
  self.assertEqual(hashlib.sha256(self.g.record_bytes('P102673')).hexdigest(),r['default_record_sha256'])
  self.assertEqual(hashlib.sha256(self.g.evidence_record_bytes('P102673')).hexdigest(),r['version_hash'])
  self.assertNotEqual(r['default_record_sha256'],r['version_hash'])
 def test_subtotal_and_evidence(self):
  p='/entries/44/measurements/0/adopted';r=self.g.research_value('P102673',p)
  self.assertEqual(r['value']['components']['count'],'177')
  self.assertIsNone(m.resolve_pointer(self.g.evidence_record('P102673'),p))
  self.assertTrue(any(x['value']=='177' for x in self.g.search('P102673','177')))
 def test_written_values_not_balanced(self):
  for sid in ('P102673','P108499','P110248','P113484','P120655','P202241'):
   raw=self.g.evidence_record(sid);current=self.g.record(sid)
   for p,v in m.walk(raw):
    if v in ('217','20') if isinstance(v,str) else False:
     self.assertEqual(m.resolve_pointer(current,p),v,(sid,p))
 def test_null_and_local_qualification(self):
  r=self.g.research_value('P100144','/document/document_type')
  self.assertIsNone(r['value']);self.assertEqual([q['id'] for q in r['qualifications']],['q5'])
 def test_originals_inspectable(self):
  raw=self.g.evidence_record('P102673');pinned=self.g._source_original(raw)
  self.assertEqual(hashlib.sha256(pinned).hexdigest(),raw['document']['source_version']['sha256'])
  self.assertNotEqual(pinned,self.g.original('P102673','registered'))
 def test_qualifications_and_alternatives(self):
  r=self.g.record('P100150')['qualifications'][0]
  self.assertNotIn('alternatives',r);self.assertIn('branch_evidence',r)
  self.assertIn('alternatives',self.g.evidence_record('P100150')['qualifications'][0])
 def test_default_endpoints(self):
  sid='P102673';r=self.g.record(sid);c=self.g.connected(sid)
  for edge in c['incidences']:
   if edge[2].startswith('reference:'):
    self.assertEqual(m.resolve_pointer(r,edge[3]),c['nodes'][edge[1]][1])
  self.assertEqual(c['identity_unions'],[])
 def test_unchanged_native_quantities(self):
  raw=self.g.evidence_record('P202241');r=self.g.record('P202241')
  for p,v in m.walk(raw):
   if p.endswith('/adopted'):self.assertEqual(m.resolve_pointer(r,p),v)
 def test_cursor(self):
  a=self.g.search_page('',source_limit=1,limit=1)
  b=self.g.search_page('',cursor=a['next_cursor'],source_limit=1,limit=1)
  self.assertEqual(a['matches']+b['matches'],list(self.g.search_all('',limit=2)))
  with self.assertRaises(ValueError):self.g.search_page('different',cursor=a['next_cursor'])
  empty=self.g.search_page('NO_SUCH_TERM_881112',source_limit=1)
  self.assertEqual(empty['matches'],[]);self.assertIsNotNone(empty['next_cursor'])
 def test_archive_is_explicit(self):
  archived=[r for r in self.g.rows('records') if not r['current']]
  self.assertEqual(len(archived),3)
  for e in archived:
   with self.assertRaises(KeyError):self.g.record(e['source_id'])
   r=self.g.research(e['source_id'],False)
   self.assertEqual(r['research_population'],'explicit_archival');self.assertFalse(r['current'])
 def test_detached_cache(self):
  r=self.g.record('P100144');r['document']['source_id']='bad'
  self.assertEqual(self.g.record('P100144')['document']['source_id'],'P100144')
 def test_isolated_runtime(self):
  p=subprocess.run([sys.executable,'-I','-S',str(READER),'--root',str(ROOT),'research','P105740','/relations/4/value/code'],capture_output=True,text=True,check=True)
  self.assertEqual(json.loads(p.stdout)['value'],'administrator')
 def test_null_ancestor_not_a_typo(self):
  r=self.g.research_value('P145460','/entries/12/participants/0/role')
  self.assertIsNone(r['value']);self.assertEqual(r['value_status'],'null_due_to_unresolved_ancestor')
  self.assertEqual(r['ancestor_pointer'],'/entries/12/participants')
  self.assertTrue(r['qualifications']);self.assertTrue(r['branches'])
  with self.assertRaises(KeyError):self.g.research_value('P145460','/entries/12/participants/0/ROLETYPO')
  with self.assertRaises((TypeError,KeyError)):self.g.pointer('P145460','/entries/12/participants/0/role')
 def test_branch_and_ambiguity_are_distinct(self):
  q=self.g.research_value('P100144','/mentions/1/search_form')
  self.assertFalse(q['has_branches']);self.assertTrue(q['has_ambiguity'])
  self.assertEqual(q['identified_branch_count'],0)
  self.assertTrue(all(not a['is_identified_branch'] and a['annotation_kind']=='qualification' for a in q['branches']))
  b=self.g.research_value('P102673','/entries/44/measurements/0/adopted')
  self.assertTrue(b['has_branches']);self.assertTrue(b['has_ambiguity'])
  self.assertTrue(any(a['is_identified_branch'] and a['annotation_kind']=='branch' for a in b['branches']))
 def test_stream_output_is_detached(self):
  row=next(self.g.iter_records());sid=row['source_id'];row['record']['document']['source_id']='MUTATED'
  self.assertEqual(next(self.g.iter_records())['record']['document']['source_id'],sid)
  match=next(self.g.search_all('',limit=1));match['value']='MUTATED'
  self.assertNotEqual(next(self.g.search_all('',limit=1))['value'],'MUTATED')
 def test_inspect_default_child_without_evidence_child(self):
  p='/entries/44/measurements/0/adopted/components/count';r=self.g.inspect('P102673',p)
  self.assertEqual(r['value'],'177');self.assertTrue(r['default_pointer_exists'])
  self.assertIsNone(r['evidence_value']);self.assertFalse(r['evidence_pointer_exists'])
  with self.assertRaises((KeyError,TypeError)):
   self.g.inspect('P102673','/entries/44/measurements/0/adopted/components/COUNTTYPO')
 def test_pointer_syntax(self):
  for p in ('bad','/~2','/entries/00'):
   with self.assertRaises((ValueError,KeyError)):m.resolve_pointer({},p)
if __name__=='__main__':unittest.main()
