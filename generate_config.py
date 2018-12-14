import ConfigParser


if __name__ == '__main__':
    cp = ConfigParser.ConfigParser()
    cp.add_section('global')
    cp.set('global', 'using_cuda', 'True')
    cp.set('global', 'epoch', '10')
    cp.set('global', 'gpu_id', '0')
    cp.set('global', 'display_iter', '10')
    cp.set('global', 'val_iter', '100')
    cp.set('global', 'save_iter', '500')
    cp.set('global', 'pretrained', 'False')
    cp.set('global', 'pretrained_model', '')
    cp.set('global', 'train_dataset', './train')
    cp.set('global', 'test_dataset', './test')
    cp.set('global', 'batch_size', '128')
    cp.set('global', 'sample_ratio', '0.5')
    cp.set('global', 'test_batch_num', '10')
    cp.set('global', 'have_prefix', 'False')
    cp.set('global', 'prefix', '')
    cp.add_section('parameter')
    cp.set('parameter', 'optimizer', 'SGD')
    cp.set('parameter', 'lr', '0.001')
    cp.set('parameter', 'momentum', '0.9')
    cp.set('parameter', 'weight_decay', '0.0005')
    cp.set('parameter', 'rho', '0.0005')
    with open('./config', 'w') as fp:
        cp.write(fp)
