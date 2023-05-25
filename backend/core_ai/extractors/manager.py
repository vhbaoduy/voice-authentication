import os
from .extractor import EmbeddingExtractor
from ..utils import LOG
import glob
import gdown

'''
    - All models are pretrained from https://github.com/TaoRuijie/ECAPA-TDNN with different configuration.
    - Get models from my thesis.
'''
URLS={
    128: 'https://drive.google.com/file/d/1k2XNHlfa9IgzLbGnvRdrQFufbXc44wex/view?usp=sharing',
    256: 'https://drive.google.com/file/d/1i_1O9ncMU59TKswWSP9FOtLiX_CCijb9/view?usp=sharing',
    512: 'https://drive.google.com/file/d/1wfrPLwIndSJsaGR7PhKtK2bIV4GMqpTY/view?usp=sharing',
    1024: 'https://drive.google.com/file/d/1DDTJQ-YNJ5tJ1dtq5ghMR9N0QqhArK3I/view?usp=sharing'
}
MODEL_TYPES = {
    1024:'ECAPA-TDNN-1024',
    512:'ECAPA-TDNN-512',
    256:'ECAPA-TDNN-256',
    128:'ECAPA-TDNN-128'
}

def get_extractor(channel,
                  path,
                  device):
    '''
        Get extractor from local
        Args:
            channel: config of model
            path: path to pretrained model
            device
    '''
    assert channel in [1024,512,256,128]
    extractor = EmbeddingExtractor(C=channel,
                                   device=device)
    try:
        extractor.load_parameters(path)
    except IOError as ex:
        LOG.error('Not found pretrained model in %s' % path)
        return None
    return extractor

def check_pretrained_models(root,channel):
    '''
        Check pretrained model in 'root'/models and download
    '''
    path = os.path.join(root,'models')
    if not os.path.exists(path):
        os.mkdir(path)
        download_model(path)
    else:
        files = glob.glob(os.path.join(root, 'models/ecapa-tdnn-*.model'))
        if len(files) == 0:
            download_model(path,channel)


def download_model(root,channel):
    '''
        Download models to $rooot/models
    '''
    url = URLS[channel]
    name = 'ecapa-tdnn-%s.model' % channel
    gdown.download(url, os.path.join(root,name),quiet=False,fuzzy=True)


def get_model_path(root,channel):
    path = os.path.join(root, 'models/ecapa-tdnn-%s.model'%channel)
    files = glob.glob(path)
    if len(files) == 0:
        LOG.info('Downloading pretrained model')
        check_pretrained_models(root, channel)
    return path

def download_all_models(root):
    for c in URLS:
        check_pretrained_models(root, c)


    
    

    
# if __name__ == '__main__':
#     check_pretrained_models('../')