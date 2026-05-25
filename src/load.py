class Load:
    def save_as_csv(self, data, output_path):
        data.to_csv(output_path, index = False)
