import voice

voice.engine.save_to_file('music mode is selected','music_mode.mp3')
voice.engine.runAndWait()
voice.engine.save_to_file('walking mode is selected','walking_mode.mp3')
voice.engine.runAndWait()

voice.engine.save_to_file('image read mode is selected', 'image_read.mp3')
voice.engine.runAndWait()

voice.engine.save_to_file('image detection mode is selected', 'image_detection.mp3')
voice.engine.runAndWait()
