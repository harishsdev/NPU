from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="microsoft/resnet-50",
    local_dir="./resnet50",
    local_dir_use_symlinks=False
)
