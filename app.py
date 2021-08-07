from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        cap_shape = (request.form["cap-shape"])
        if (cap_shape == "b"):
            b = 0
        elif (cap_shape == "c"):
            c = 1
        elif (cap_shape == "f"):
            f = 2
        elif (cap_shape == "k"):
            k = 3
        elif (cap_shape == "s"):
            s = 4
        elif (cap_shape == "x"):
            x = 5
        

        cap_surface = request.form["cap-surface"]
        if (cap_surface == "f"):
            f = 0
        elif (cap_surface == "g"):
            g = 1
        elif (cap_surface == "x"):
            x = 2
        elif (cap_surface == "y"):
            y = 3
        elif (cap_surface == "s"):
            s = 4
        
        cap_color = request.form["cap-color"]
        if (cap_color == "b"):
            b = 0
        elif (cap_color == "c"):
            c = 1
        elif (cap_color == "e"):
            e = 2
        elif (cap_color == "g"):
            g = 3
        elif (cap_color == "n"):
            n = 4
        elif (cap_color == "p"):
            p = 5
        elif (cap_color == "r"):
            r = 5
        elif (cap_color == "u"):
            u = 5
        elif (cap_color == "w"):
            w = 5
        elif (cap_color == "y"):
            y = 5
                
        bruises = request.form["bruises"]
        if (bruises == "f"):
            f = 0
        elif (bruises == "t"):
            t = 1
        
        odor = request.form["odor"]
        if (odor == "a"):
            a = 0
        elif (odor == "c"):
            c = 1
        elif (odor == "f"):
            f = 2
        elif (odor == "l"):
            l = 3
        elif (odor == "m"):
            m = 4
        elif (odor == "n"):
            n = 5
        elif (odor == "p"):
            p = 6
        elif (odor == "s"):
            s = 7
        elif (odor == "y"):
            y = 8
        
        gill_attachment = request.form["gill-attachment"]
        if (gill_attachment == "a"):
            a = 0
        elif (gill_attachment == "d"):
            d = 1
        elif (gill_attachment == "f"):
            f = 2    
        elif (gill_attachment == "n"):
            n = 3   
        
        gill_spacing = request.form["gill-spacing"]
        if (gill_spacing == "c"):
            c = 0
        elif (gill_spacing == "d"):
            d = 1
        elif (gill_spacing == "w"):
            w = 2        
        
        gill_size = request.form["gill-size"]
        if (gill_size == "b"):
            b = 0
        elif (gill_size == "n"):
            n = 1
        
        gill_color = request.form["gill-color"]
        if (gill_color == "b"):
            b = 0
        elif (gill_color == "e"):
            e = 1
        elif (gill_color == "g"):
            g = 2
        elif (gill_color == "h"):
            h = 3
        elif (gill_color == "k"):
            k = 4
        elif (gill_color == "n"):
            n = 5
        elif (gill_color == "o"):
            o = 6
        elif (gill_color == "p"):
            p = 7
        elif (gill_color == "r"):
            r = 8
        elif (gill_color == "u"):
            u = 9
        elif (gill_color == "w"):
            w = 10
        elif (gill_color == "y"):
            y = 11
   
        stalk_shape = request.form["stalk-shape"]
        if (stalk_shape == "e"):
            e = 0
        elif (stalk_shape == "t"):
            t = 1
        
        stalk_root = request.form["stalk-root"]
        if (stalk_root == "b"):
            b = 0
        elif (stalk_root == "c"):
            c = 1
        elif (stalk_root == "e"):
            e = 2
        elif (stalk_root == "r"):
            r = 3
        elif (stalk_root == "u"):
            u = 4
        elif (stalk_root == "z"):
            z = 5

        stalk_surface_above_ring = request.form["stalk-surface-above-ring"]
        if (stalk_surface_above_ring == "f"):
            f = 0
        elif (stalk_surface_above_ring == "k"):
            k = 1
        elif (stalk_surface_above_ring == "s"):
            s = 2
        elif (stalk_surface_above_ring == "y"):
            y = 3
        
        stalk_surface_below_ring = request.form["stalk-surface-below-ring"]
        if (stalk_surface_below_ring == "f"):
            f = 0
        elif (stalk_surface_below_ring == "k"):
            k = 1
        elif (stalk_surface_below_ring == "s"):
            s = 2
        elif (stalk_surface_below_ring == "y"):
            y = 3
        
        stalk_color_above_ring = request.form["stalk-color-above-ring"]
        if (stalk_color_above_ring == "b"):
            b = 0
        elif (stalk_color_above_ring == "c"):
            c = 1
        elif (stalk_color_above_ring == "e"):
            e = 2
        elif (stalk_color_above_ring == "g"):
            g = 3
        elif (stalk_color_above_ring == "n"):
            n = 4
        elif (stalk_color_above_ring == "o"):
            o = 5
        elif (stalk_color_above_ring == "p"):
            p = 6
        elif (stalk_color_above_ring == "w"):
            w = 7
        elif (stalk_color_above_ring == "y"):
            y = 8
            
        stalk_color_below_ring = request.form["stalk-color-below-ring"]
        if (stalk_color_below_ring == "b"):
            b = 0
        elif (stalk_color_below_ring == "c"):
            c = 1
        elif (stalk_color_below_ring == "e"):
            e = 2
        elif (stalk_color_below_ring == "g"):
            g = 3
        elif (stalk_color_below_ring == "n"):
            n = 4
        elif (stalk_color_below_ring == "o"):
            o = 5
        elif (stalk_color_below_ring == "p"):
            p = 6
        elif (stalk_color_below_ring == "w"):
            w = 7
        elif (stalk_color_below_ring == "y"):
            y = 8
           
        veil_color = request.form["veil-color"]
        if (veil_color == "n"):
            n = 0
        elif (veil_color == "o"):
            o = 1
        elif (veil_color == "w"):
            w = 2
        elif (veil_color == "y"):
            y = 3
        
        ring_number = request.form["ring-number"]
        if (ring_number == "n"):
            n = 0
        elif (ring_number == "o"):
            o = 1
        elif (ring_number == "t"):
            t = 2
        
        ring_type = request.form["ring-type"]
        if (ring_type == "c"):
            c = 0
        elif (ring_type == "e"):
            e = 1
        elif (ring_type == "f"):
            f = 2
        elif (ring_type == "l"):
            l = 3
        elif (ring_type == "n"):
            n = 4
        elif (ring_type == "p"):
            p = 5
        elif (ring_type == "s"):
            self = 6
        elif (ring_type == "z"):
            z = 7
        
        spore_print_color = request.form["spore-print-color"]
        if (spore_print_color == "b"):
            b = 0
        elif (spore_print_color == "h"):
            h = 1
        elif (spore_print_color == "k"):
            k = 2
        elif (spore_print_color == "n"):
            n = 3
        elif (spore_print_color == "o"):
            o = 4
        elif (spore_print_color == "r"):
            r = 5
        elif (spore_print_color == "u"):
            u = 6
        elif (spore_print_color == "w"):
            w = 7   
        elif (spore_print_color == "y"):
            y = 8

        population = request.form["population"]
        if (population == "a"):
            a = 0
        elif (population == "c"):
            c = 1
        elif (population == "n"):
            n = 2
        elif (population == "s"):
            s = 3
        elif (population == "v"):
            v = 4
        elif (population == "y"):
            y = 5
        
        habitat = request.form["habitat"]
        if (habitat == "d"):
            d = 0
        elif (habitat == "g"):
            g = 1
        elif (habitat == "l"):
            l = 2
        elif (habitat == "m"):
            m = 3
        elif (habitat == "p"):
            p = 4
        elif (habitat == "u"):
            u = 5
        elif (habitat == "w"):
            w = 5
        
    
        
        
        prediction=model.predict([[cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment, gill_spacing, gill_size, gill_color, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring, stalk_color_below_ring, veil_color, ring_number, ring_type, spore_print_color, population, habitat]])
            
        
    
        output=round(prediction[0],2)
        if output == 1:
            output = "Not Edible"
        else:
            output = "Edible"

        return render_template('home.html',prediction_text="The mushroom is. {}".format(output))

    return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)