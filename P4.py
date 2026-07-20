from jiwer import cer
ground_truth = "नमस्ते दुनिया"
ocr_output = "नमस्त दुनिया" # Simulating an error
error = cer(ground_truth, ocr_output)
print(f"Character Error Rate: {error * 100}%")
