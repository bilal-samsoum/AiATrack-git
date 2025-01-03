class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/b/PycharmProjects/AiATrack-git'  # Base directory for saving network checkpoints
        self.tensorboard_dir = self.workspace_dir  # Directory for tensorboard files
        self.pretrained_networks = self.workspace_dir + '/pretrained_networks'
        self.lasot_dir = 'PATH/LaSOT'
        self.got10k_dir = '/home/b/AiATrack2/GOT-10k/train'
        self.trackingnet_dir = 'PATH/TrackingNet'
        self.coco_dir = 'PATH/COCO'
