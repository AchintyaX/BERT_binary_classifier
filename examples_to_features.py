class InputFeatures(object):
	""" A single set of features of data """

	def __init__(self, input_ids, input_mask, segment_ids, label_id):
		self.input_ids = input_ids
		self.input_mask = input_mask
		self.segment_ids = segment_ids
		self.label_ids = label_id

	def _truncate_seq_pair(tokens_a, tokens_b, max_length):
		""" Truncate a sequence pair in place to the max length """

		# this is a simple heuristic which will always truncate the longer sequence 
		# one token at a time. THis makes more sense than truncating an equal percent 
		# of tokens from each, since if one sequence is very short then each token
		# that's truncated likely contains more info than a longer sequence 

		while True:
			total_length = len(tokens_a) + len(tokens_b)
			if total_length <= max_length:
				break
			if len(tokens_a) > len(tokens_b):
				tokens_a.pop()
			else:
				tokens_b.pop()

	def convert_examples_to_feature(example_row):
		# return example row

		example, label_map, max_seq_length, tokenizer, output_mode = example_row

		tokens_a = tokenizer.tokenize(example.text_a)
		