import re

from typing import Optional

from metadata import Metadata, MetadataPlugin


class CuckooBinariesMetadata(MetadataPlugin):
    is_extractor = True

    def identify(self, matched_fname: str) -> Optional[str]:
        m = re.search(r"/binaries/([a-f0-9]+)$", matched_fname)
        return m[1] if m else None

    def extract(
        self, identifier: str, matched_fname: str, current_meta: Metadata
    ) -> Metadata:
        return {"cuckoo_hash": {"value": identifier}}
