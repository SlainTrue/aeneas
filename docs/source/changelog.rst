Changelog
=========

v1.2.0 (2015-09-27)
-------------------

#. Added ``sd.py`` to automatically detect the head/tail/interval of an audio file
#. Added the corresponding ``aeneas.tools.run_sd`` utility
#. Added the corresponding Task configuration parameters: ``is_audio_file_detect_head_min``, ``is_audio_file_detect_head_max``, ``is_audio_file_detect_tail_min``, ``is_audio_file_detect_tail_max``, and ``os_task_file_head_tail_format``
#. Added ``SMILH`` and ``SMILM`` sync map output formats (``SMIL`` becoming an alias of ``SMILH``)
#. Added ``CSVM``, ``SSVM``, ``TSVM``, and ``TXTM`` formats (``CSV``, ``SSV``, ``TSV``, and ``TXT`` becoming their aliases)
#. Renamed the previous ``JSON`` sync map output format to ``RBSE``
#. Added a new ``JSON`` format
#. Renamed the previous ``XML`` sync map output format to ``XML_LEGACY``
#. Changed ``JSON`` (and ``RBSE``) write function, now using the ``json`` library
#. Added a new ``XML`` format
#. Changed ``SMIL``, ``TTML``, and ``XML`` write functions, now using the ``lxml`` library
#. Added functions to read sync map files
#. Added the ``aeneas.tools.convert_syncmap`` utility to convert sync maps
#. Added ``reverse``, ``trim``, and ``write`` functions to ``AudioFile``
#. Added all the languages that espeak v1.48.03 supports to the ``Language`` enumeration (those not tested yet are marked as such)
#. Marked Persian (``fa``) and Swahili (``sw``) languages as tested
#. Added the ``aeneas.tools.synthesize_text`` utility to synthesize multiple fragments into a single wave file
#. Changed ``FFMPEG_PARAMETERS_DEFAULT`` in ``ffmpeg.py`` to ``FFMPEG_PARAMETERS_SAMPLE_22050`` (i.e., from 44100 Hz to 22050 Hz)
#. Fixed the ``TTML`` output
#. Fixed a ``KeyError`` bug in ``ffprobewrapper.py`` when probing a file not recognized as audio file
#. Fixed a bug in ``cdtw.c``: int overflow when computing the ``centers`` array on long (>30 minutes) audio files
#. Many unit tests have been rewritten, extended, or refactored
#. Other minor fixes and code/documentation improvements

v1.1.2 (2015-09-24)
-------------------

#. Better ``setup.py``, especially for Windows users (courtesy of David Smith)

v1.1.1 (2015-08-23)
-------------------

#. Added ``compile_c_extensions.bat`` and directions for Windows users (courtesy of Richard Margetts)
#. Added warning to ``aeneas.tools.*`` when running without Python C Extensions compiled
#. Improved ``README.md``

v1.1.0 (2015-08-21)
-------------------

#. Added ``cdtw`` C module for running the DTW much faster than in pure Python (falling back to Python if ``cdtw`` cannot be load)
#. Added ``cmfcc`` C module for extracting the MFCCs much faster than in pure Python (falling back to Python if ``cmfcc`` cannot be load)
#. Moved code for extracting MFCCs into ``AudioFile``, and rewritten ``dtw.py`` and ``vad.py`` accordingly
#. Added ``aeneas.tools.extract_mfcc`` utility
#. Rewritten the ``STRIPE`` and ``EXACT`` (Python) algorithms to compute the accumulated cost matrix in place
#. Renamed ``ALIGNER_USE_EXACT_ALGO_WHEN_MARGIN_TOO_LARGE`` to ``ALIGNER_USE_EXACT_ALGORITHM_WHEN_MARGIN_TOO_LARGE``
#. Removed ``STRIPE_NOT_OPTIMIZED`` algorithm from ``dtw.py``
#. Added the ``OFFSET`` and ``RATEAGGRESSIVE`` boundary adjustment algorithms
#. Cleaned the code for ``RATE`` boundary adjustment algorithm
#. Other minor fixes and code/docs improvements

v1.0.4 (2015-08-09)
-------------------

#. Added boundary adjustment algorithm
#. Added VAD algorithm and ``aeneas.tools.run_vad`` utility
#. Added ``subtitles`` input text format and the ability of dealing with multiline text fragments
#. Added ``SSV`` output format
#. Added ``CSVH``, ``SSVH``, ``TSVH``, ``TXTH`` output formats (i.e., human-readable variants)
#. Added ``-v`` option to ``aeneas.tools.execute_task`` and ``aeneas.tools.execute_job`` to produce verbose output
#. Added ``install_dependencies.sh``
#. Added this changelog
#. Sanitized log messages, fixing a problem with ``tee=True`` crashing in non UTF-8 shells (tested in a POSIX shell)
#. Improved unit tests
#. Other minor fixes and code/docs improvements

v1.0.3 (2015-06-13)
-------------------

#. Added ``TSV`` output format
#. Added reference to ``aeneas-vagrant``
#. Added ``run_all_unit_tests.sh``

v1.0.2 (2015-05-14)
-------------------

#. Corrected typos
#. Merged ``requirements.txt``

v1.0.1 (2015-05-12)
-------------------

#. Initial version


