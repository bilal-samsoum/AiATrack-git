from lib.test.evaluation.environment import EnvSettings


def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here

    settings.got10k_path = '/home/b/AiATrack2/GOT10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_path = 'PATH/LaSOT'
    settings.network_path = '/home/b/PycharmProjects/AiATrack-git/test/networks'  # Where tracking networks are stored
    settings.nfs_path = 'PATH/NFS30'
    settings.otb_path = 'PATH/OTB100'
    settings.prj_dir = '/home/b/PycharmProjects/AiATrack-git'
    settings.result_plot_path = '/home/b/PycharmProjects/AiATrack-git/test/result_plots'
    settings.results_path = '/home/b/PycharmProjects/AiATrack-git/test/tracking_results'  # Where to store tracking results
    settings.save_dir = '/home/b/PycharmProjects/AiATrack-git'
    settings.segmentation_path = '/home/b/PycharmProjects/AiATrack-git/test/segmentation_results'
    settings.tn_packed_results_path = ''
    settings.trackingnet_path = 'PATH/TrackingNet'
    settings.uav_path = '/home/b/AiATrack2/UAV123/Dataset_UAV123_2/UAV123'
    settings.show_result = False
    return settings
