class Param():
    
    def __init__(self, args):
        
        self.hyper_param = self.get_hyper_parameters(args)

    def get_hyper_parameters(self, args):
        """
        Args:
            bert_model (directory): The path for the pre-trained bert model.
            max_seq_length (autofill): The maximum total input sequence length after tokenization. Sequences longer than this will be truncated, sequences shorter will be padded.
            num_train_epochs (int): The number of training epochs.
            num_labels (autofill): The output dimension.
            freeze_bert_parameters (binary): Whether to freeze all parameters but the last layer.
            feat_dim (int): The feature dimension.
            warmup_proportion (float): The warmup ratio for learning rate.
            lr (float): The learning rate of backbone.
            loss_fct (str): The loss function for training.
            activation (str): The activation function of the hidden layer (support 'relu' and 'tanh').
            freeze_bert_parameters (binary): Whether to freeze all parameters but the last layer.
            train_batch_size (int): The batch size for training.
            eval_batch_size (int): The batch size for evaluation. 
            test_batch_size (int): The batch size for testing.
            wait_patient (int): Patient steps for Early Stop.
        """
        hyper_parameters = {

            'bert_model': "bert-base-uncased", # "bert-base-uncased", bert-base-chinese
            'max_seq_length': None,
            'num_train_epochs': 10, #100,
            'num_labels': None,
            'freeze_bert_parameters': False, #True,
            'feat_dim': 768,
            'warmup_proportion': 0.1,
            'lr': 5e-5, #2e-5,
            'activation': 'relu',
            'loss_fct': 'MCL',
            'train_batch_size': 128,
            'eval_batch_size': 64,
            'test_batch_size': 64,
            'wait_patient': 3 #10
        }


        return hyper_parameters