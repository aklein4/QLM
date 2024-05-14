import torch
import torch.nn as nn
import torch.nn.functional as F

from trainers.base_xla_trainer import BaseXLATrainer
from utils.data_utils import DotDict
from  utils.training_utils import loss, ppl, acc, pcorr


class XLALMTrainer(BaseXLATrainer):


    def train_step(self, model, x, tokenizer):
        out = model(x)
        ignore_index = tokenizer.pad_token_id

        results = DotDict(
            lm_loss=loss(out["lm_logits"], x, ignore_index),
            lm_ppl=ppl(out["lm_logits"], x, ignore_index),
            lm_acc=acc(out["lm_logits"], x, ignore_index),
            lm_pcorr=pcorr(out["lm_logits"], x, ignore_index),
        )
        results.loss = results.lm_loss

        return results
