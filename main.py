import ext_fns

# 1. Get our saved songs (track urls? ids?)
scopes = ['user-library-read', 'user-read-playback-state','user-modify-playback-state']

sp = ext_fns.connect(scopes)

# result = sp.current_user_saved_tracks(limit=20,market="US")

#print(sp.audio_features('3O5JIwSON3KBaoyMUsjLjn'))

sp.next_track(device_id='97df809cc9f89751478b3c309e7c6fb1f61d8d62')
# sp.start_playback(device_id='97df809cc9f89751478b3c309e7c6fb1f 61d8d62')


# for x,i in enumerate(ext_fns.resolve_tracks(sp, result)):
#     print(x,i,'\n')

'''
TODO: Explore track audio features?
    : Audio analysis

'''


# 2. Create playlists and add tracks according to some criteria??

# 3. Refresh data??