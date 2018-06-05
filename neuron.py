
class Neuron:
	input_sum = 0.0

	def setInput(self, input):
		self.input_sum += input
		print(str(self.input_sum))


class NeuralNetwork:
	neuron = Neuron()

	def commit(self, input_data):
		for data in input_data:
			self.neuron.setInput(data)


neural_network = NeuralNetwork()

trial_data = [1.0, 2.0, 3.0]
neural_network.commit(trial_data)



