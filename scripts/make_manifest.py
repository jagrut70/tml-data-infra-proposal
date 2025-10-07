import json, argparse, time, hashlib

parser = argparse.ArgumentParser()
parser.add_argument("--seed", default="demo")
args = parser.parse_args()

manifest = {
  "dataset_id": f"text_catalog_{int(time.time())}",
  "version": "0.1.0",
  "filters": {"lang": ["en"], "length_tokens_lt": 4096},
  "sources": ["bronze_raw_web"],
  "build": {"dedup": ["sha256","minhash","ann"], "exclude": ["pii","unsafe"]}
}
payload = json.dumps(manifest, sort_keys=True).encode("utf-8")
manifest["manifest_sha"] = hashlib.sha256(payload).hexdigest()

print(json.dumps(manifest, indent=2))
