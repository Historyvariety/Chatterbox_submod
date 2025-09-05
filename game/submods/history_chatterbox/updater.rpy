# This lets SUP (Submod Updater Plugin) update your submod automatically.

init -989 python:
    if hasattr(store, "mas_submod_utils") and store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="history_chatterbox",          # MUST match your folder name in game/Submods
            user_name="historyvariety",           # Your GitHub username
            repository_name="Chatterbox_submod",  # Your repo name (not the full URL)
            repository_url="https://github.com/Historyvariety/Chatterbox_submod",
            extraction_depth=3                    # Most likely 3 (see below)
        )

# Optional but recommended: version number
define history_chatterbox_version = "1.0.0"
