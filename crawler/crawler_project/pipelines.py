import hashlib
from datetime import datetime

class HashAndStampPipeline:
    def process_item(self, item, spider):
        body = (item.get("html") or "").encode("utf-8", errors="ignore")
        item["sha256"] = hashlib.sha256(body).hexdigest()
        item["fetch_ts"] = item.get("fetch_ts") or datetime.utcnow().isoformat()+"Z"
        return item
