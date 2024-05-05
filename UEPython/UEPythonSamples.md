#------------------------------------------------------------------------------------------
#UEPythonのスクリプトのサンプル
#一部はgaruさんの備忘録より転載
import unreal
#------------------------------------------------------------------------------------------
# フォルダに入っているアセット取得 ★
assets = unreal.EditorAssetLibrary.list_assets(path)
#テストコード
path = "/Game/Developers"
assets = unreal.EditorAssetLibrary.list_assets(path)
print(assets)
#------------------------------------------------------------------------------------------
# アセットが存在するか　★
unreal.EditorAssetLibrary.does_asset_exist(path)
import unreal
#テストコード
asset_path = "/Game/Developers/BP_test"
exists = unreal.EditorAssetLibrary.does_asset_exist(asset_path)
print(f"アセットが存在するか: {exists}")
#------------------------------------------------------------------------------------------
# world取得 サブシステム移行済★
editor_subsystem = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
world = editor_subsystem.get_editor_world()
print (world)
#------------------------------------------------------------------------------------------
# 開いているSequencerを閉じる　★
unreal.LevelSequenceEditorBlueprintLibrary.close_level_sequence()
#------------------------------------------------------------------------------------------
# Import Animation Sequence
lTask = []
task = unreal.AssetImportTask()
task.automated = True
task.destination_path = destination_path #インポートしたアセットを保存するパス。
task.filename = filename #インポートするFBXファイルの名前。
task.replace_existing = True #既存のアセットを置き換えるかどうか。
task.save = True #インポート後にアセットを保存するかどうか。
task.options = unreal.FbxImportUI() #インポートオプションを設定するための unreal.FbxImportUI() インスタンス。
task.options.import_animations = True #アニメーションをインポートするかどうか。
task.options.skeleton = skeleton #使用するスケルトンアセット。
task.options.mesh_type_to_import = unreal.FBXImportType.FBXIT_ANIMATION #インポートするメッシュのタイプ（ここではアニメーション）。
lTask.append(task)
unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(lTask)
#------------------------------------------------------------------------------------------
# 今開いているレベルシーケンサーを取得
level_sequence = unreal.LevelSequenceEditorBlueprintLibrary.get_current_level_sequence()
print (level_sequence)
#------------------------------------------------------------------------------------------
# レベル上のすべてのバインディングを取得
bindings = level_sequence.get_bindings()
print (bindings)
# バインディングからアクター名を取得してプリント
for binding in bindings:
    print(f"Actor Name: {binding.get_name()}")
#------------------------------------------------------------------------------------------
# レベルシーケンサーに新しいフォルダを追加
new_folder_name = "aaa"
new_folder = unreal.MovieSceneSequenceExtensions.add_root_folder_to_sequence(level_sequence, new_folder_name)
#------------------------------------------------------------------------------------------
# レベル上の各バインディングからトラックを取得
for binding in bindings:
    tracks = binding.get_tracks()

# レベル上の各バインディングからトラックを取得しMovieSceneSkeletalAnimationTrackのパラメータを取得(要はアニメーションのトラックのパラメータ)
for binding in bindings:
    tracks = binding.get_tracks()
    for track in tracks:
        if isinstance(track, unreal.MovieSceneSkeletalAnimationTrack):
            sections = track.get_sections()
            for section in sections:
                params = section.get_editor_property("Params")
                if params:
                    # Params の内容を表示
                    print("Animation: {}".format(params.animation))
                    print("Start Frame Offset: {}".format(params.start_frame_offset)).0.
                    print("End Frame Offset: {}".format(params.end_frame_offset))
                    print("Play Rate: {}".format(params.play_rate))
                    print("Reverse: {}".format(params.reverse))
                    print("Slot Name: {}".format(params.slot_name))
#------------------------------------------------------------------------------------------
# Create Level Sequence★
asset_name = "LS_test_aaa" #シーケンサーアセットの名前をきめる
package_path = "/Game/Developers" #作る場所を指定

sq = unreal.AssetToolsHelpers.get_asset_tools().create_asset(
                asset_name,
                package_path,
                unreal.LevelSequence,
                unreal.LevelSequenceFactoryNew())

# フレームレート設定
sq.set_display_rate(unreal.FrameRate(integer))

# インアウト設定（フレーム）
sq.set_playback_start(integer)
sq.set_playback_end(integer)

# ビューレンジ（秒）
sq.set_view_range_start(float)
sq.set_view_range_end(float)

# ワークレンジ設定（秒）
sq.set_work_range_start(float)
sq.set_work_range_end(float)

# Level Sequenceを開く
unreal.LevelSequenceEditorBlueprintLibrary.open_level_sequence(sq)
# カレントフレーム設定
unreal.LevelSequenceEditorBlueprintLibrary.set_current_time(integer)

#------------------------------------------------------------------------------------------
# Get Bone Name ★
# スケルタルメッシュからスケルトンを取得し、スケルトンモディファイアからget_all_bone_namesで取得
skeleton = asset.skeleton
if skeleton is not None:
    skeleton_modifier = unreal.SkeletonModifier()
    success = skeleton_modifier.set_skeletal_mesh(asset)
    if success:
        all_bone_names = skeleton_modifier.get_all_bone_names()
        for bone_name in all_bone_names:
            print(bone_name)
#------------------------------------------------------------------------------------------
# Get Socket Name ★
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
for asset in selected_assets:
    if isinstance(asset, unreal.SkeletalMesh):
        num_sockets = asset.num_sockets()
        for i in range(num_sockets):
            socket = asset.get_socket_by_index(i)
            print("Socket name: ", socket.socket_name)

