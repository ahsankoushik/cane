import voice_command.old_vopice as old_vopice

old_vopice.engine.save_to_file('music mode is selected','music_mode.mp3')
old_vopice.engine.runAndWait()
old_vopice.engine.save_to_file('walking mode is selected','walking_mode.mp3')
old_vopice.engine.runAndWait()

old_vopice.engine.save_to_file('image read mode is selected', 'image_read.mp3')
old_vopice.engine.runAndWait()

old_vopice.engine.save_to_file('image detection mode is selected', 'image_detection.mp3')
old_vopice.engine.runAndWait()
