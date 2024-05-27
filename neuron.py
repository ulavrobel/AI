import numpy as np
import matplotlib.pyplot as plt


class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        if weights:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

    def _f(self, x):
        return max(x * 0.1, x)

    def __call__(self, xs):
        return self._f(xs @ self.ws + self.b)


class NeuralNetwork:
    def __init__(self, layers):
        self.input_sizes = layers[:-1]
        self.n_neurons_size = layers[1:]
        self.layers = []
        for n_input, n_neuron in zip(self.input_sizes, self.n_neurons_size):
            layer = [Neuron(n_input) for _ in range(n_neuron)]
            self.layers.append(layer)

    def build_nn(self, X):
        for layer in self.layers:
            X = np.array([neuron(X) for neuron in layer])
        return X

    def draw(self):
        fig, ax = plt.subplots(figsize=(12, 12))
        layer_sizes = [self.input_sizes[0]] + [len(layer) for layer in self.layers]

        # odstępy
        v_spacing = 1.0 / float(max(layer_sizes)+1)
        h_spacing = 1.0 / float(len(layer_sizes)+0.5)

        #pozycje neuronów
        positions = []

        for i, layer_size in enumerate(layer_sizes):
            layer_pos = []
            # Wsółrzędne neuronów
            for j in range(layer_size):
                x = i * h_spacing + 0.1
                y = v_spacing * (layer_size - 1) / 2. + 1 / 2 - j * v_spacing
                layer_pos.append((x, y))
            positions.append(layer_pos)

        # Rysowanie neuronów
        for i, (layer_pos, layer_size) in enumerate(zip(positions, layer_sizes)):
            for (x, y) in layer_pos:
                if i == 0:
                    color = 'red'
                elif i == len(layer_sizes) - 1:
                    color = 'green'
                else:
                    color = 'lightblue'
                circle = plt.Circle((x, y), v_spacing / 4, color=color, ec='black', zorder=4)
                ax.add_artist(circle)

        # Rysowanie połączeń pomiędzy neuronami
        for i, (layer_pos, next_layer_pos) in enumerate(zip(positions[:-1], positions[1:])):
            for (x1, y1) in layer_pos:
                for (x2, y2) in next_layer_pos:
                    line = plt.Line2D([x1, x2], [y1, y2], color='gray')
                    ax.add_artist(line)

        # Dodanie napisów
        layer_labels = ['Input Layer'] + [f'Hidden Layer {i}' for i in range(1, len(layer_sizes) - 1)] + ['Output Layer']
        for i, label in enumerate(layer_labels):
            x, y = positions[i][0]
            plt.text(x, 0, label, horizontalalignment='center', fontsize=12, fontweight='bold')

        ax.axis('off')
        plt.show()


layers = [3, 4, 4, 1]
network = NeuralNetwork(layers)

input_data = np.array([0.79, 0.15, -0.93])
output_data = network.build_nn(input_data)
print(f'Input: {input_data}')
print(f'Output: {output_data}')

network.draw()