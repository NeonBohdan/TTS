from TTS.tts.utils.text.phonemizers.base import BasePhonemizer
from TTS.tts.utils.text.phonemizers.espeak_wrapper import ESpeak
from TTS.tts.utils.text.phonemizers.ja_jp_phonemizer import JA_JP_Phonemizer

PHONEMIZERS = {b.name(): b for b in (ESpeak, JA_JP_Phonemizer)}


ESPEAK_LANGS = list(ESpeak.supported_languages().keys())


# Dict setting default phonemizers for each language
DEF_LANG_TO_PHONEMIZER = dict()


# Add ESpeak languages and override any existing ones
_ = [ESpeak.name()] * len(ESPEAK_LANGS)
_new_dict = dict(list(zip(list(ESPEAK_LANGS), _)))
DEF_LANG_TO_PHONEMIZER.update(_new_dict)

# Force default for some languages
DEF_LANG_TO_PHONEMIZER["en"] = DEF_LANG_TO_PHONEMIZER["en-us"]
DEF_LANG_TO_PHONEMIZER["ja-jp"] = JA_JP_Phonemizer.name()


def get_phonemizer_by_name(name: str, **kwargs) -> BasePhonemizer:
    """Initiate a phonemizer by name

    Args:
        name (str):
            Name of the phonemizer that should match `phonemizer.name()`.

        kwargs (dict):
            Extra keyword arguments that should be passed to the phonemizer.
    """
    if name == "espeak":
        return ESpeak(**kwargs)
    if name == "ja_jp_phonemizer":
        return JA_JP_Phonemizer(**kwargs)
    raise ValueError(f"Phonemizer {name} not found")


if __name__ == "__main__":
    print(DEF_LANG_TO_PHONEMIZER)
