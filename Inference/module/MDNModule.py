import tensorflow as tf

from Common.Module import Module

from Inference.model.MDN import MDN

class MDNModule(Module):
    def __init__(self,nfeature,ncomp,nparam,optimizer,):
        self.nfeature = nfeature
        self.ncomp = ncomp
        self.nparam = nparam
        self.model = MDN(nfeature,ncomp,nparam)
        self.optimizer = optimizer

    def analyze(self,data,training,cfg):
        with tf.GradientTape() as tape:
            pred = self.model(cfg.inputs)
            ll = tf.math.abs(tf.math.log(self.model.calculate_loss(pred,cfg.pois)))
            ll = tf.reduce_mean(ll)
        grad = tape.gradient(ll,self.model.trainable_weights)
        self.optimizer.apply_gradients(zip(grad,self.model.trainable_weights))
        training.report.misc_str = "Loss: {0:6.2f}".format(ll)
