init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="History's Chatterbox Submod",
            user_name="historyvariety",
            repository_name="https://github.com/Historyvariety/Chatterbox_submod/tree/main",
            extraction_depth=3 # 3 if your .zip has game/Submods/MySubmod structure, 2 if just Submods/MySubmod
        )
