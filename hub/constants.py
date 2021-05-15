BYTE_PADDING = b"\0"

# number of bytes per unit
KB = 1024
MB = 1024 * KB
GB = 1024 * MB

MIN_MEMORY_CACHE_SIZE = 32 * MB
MIN_LOCAL_CACHE_SIZE = 160 * MB

CHUNKS_FOLDER = "chunks"
META_FILENAME = "meta.json"
INDEX_MAP_FILENAME = "index_map.json"

PYTEST_MEMORY_PROVIDER_BASE_ROOT = "PYTEST_TMPDIR/memory_storage_provider/"
PYTEST_LOCAL_PROVIDER_BASE_ROOT = "PYTEST_TMPDIR/local_storage_provider/"
PYTEST_S3_PROVIDER_BASE_ROOT = "snark-test/hub-2.0/"  # TODO: new bucket
