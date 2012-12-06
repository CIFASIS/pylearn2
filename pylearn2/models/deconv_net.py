from pylearn2.models.model import Model
from pylearn2.costs.cost import Cost
from pylearn2.costs.cost import FixedVarDescr
from pylearn2.spaces import Conv2DSpace
from pylearn2.utils import sharedX

class DeconvNet(Model):
    """
    A deconvolutional network.
    TODO add paper reference
    """

    def __init__(self, batch_size, input_shape, input_channels,
            hid_shape, hid_channels):

        self.__dict__.update(locals())
        del self.self

        self.input_space = Conv2DSpace(input_shape, input_channels)
        self.output_space = Conv2DSpace(hid_shape, hid_channels)


class InferenceCallback(object):

    def __init__(self, model, code):
        self.__dict__.update(locals())
        del self.self

    def __call__(self, X, Y):

        # X is a tensor for the input image of shape (batch_size, rows, cols, channels)
        # the deconv net is available as self.model
        # we need to update self.code

        raise NotImplementedError()

class DeconvNetMSESparsity(Cost):
    """
    The standard cost for training a deconvolution network.

    """

    def __call__(self, model, X, Y=None, code=None, **kwargs):

        # Training algorithm should always supply the code
        assert code is not None

        # We need to return the mean squared error
        raise NotImplementedError()

    def get_fixed_var_descr(self, model, X, Y):

        rval = FixedVarDescr()

        code = sharedX(model.output_space.get_origin_batch(model.batch_size))

        rval.fixed_vars = {'deconv_net_code' : code}

        rval.on_load_batch = [InferenceCallback(model, code)]

        return rval
