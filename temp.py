plant_dict = {'apple': 'Apple', 'cherry': 'Cherry', 'corn': 'Corn', 'grape': 'Grape', 'pepper_bell': 'Paper Bell',
              'potato': 'Potato',
              'strawberry': 'Strawberry', 'tea': 'Tea', 'tomato': 'Tomato'}

classes_dict = {'apple': ['Scab', 'Black Rot', 'Cedar Apple Rust', 'Healthy'],
                'cherry': ['Healthy', 'Powdery Mildew'],
                'corn': ['Blight', 'Common Rust', 'Gray Leaf Spot', 'Healthy'],
                'grape': ['Black Rot', 'Black Measles', 'Healthy', 'Leaf Blight Isariopsis Leaf Spot'],
                'pepper_bell': ['Bacterial Spot', 'Healthy'],
                'potato': ['Early Blight', 'Healthy', 'Late Blight'],
                'strawberry': ['Healthy', 'Leaf Scorch'],
                'tea': ['Agal Leaf', 'Anthracnose', 'Bird Eye Spot', 'Brown Blight', 'Healthy', 'Red Leaf Spot'],
                'tomato': ['Late Blight', 'Bacterial Spot', 'Early Blight', 'Healthy', 'Leaf Mold', 'Mosaic Virus',
                           'Septoria Leaf Spot', 'Spider Mites Two Spotted Spider Mite', 'Target Spot']}

print(classes_dict['tea'][2])
