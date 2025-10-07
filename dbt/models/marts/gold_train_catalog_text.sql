select
  doc_id,
  split,
  partition,
  curation_reason
from {{ ref('seed_gold_manifest') }}
