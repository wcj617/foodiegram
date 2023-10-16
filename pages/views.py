from django.views.generic import TemplateView
from .models import Food
from django.http import JsonResponse
from django.views import View


class HomePageView(TemplateView):
    template_name = "pages/home.html"

#['acorn squash', 'almond', 'amaranth', 'anchovy', 'antipasto', 'apple', 'apple pie', 'apple sauce', 'apricot', 'artichoke', 'arugula', 'asparagus', 'aspic', 'avocado', 'baby back ribs', 'bacon', 'bagel', 'baguette', 'baked alaska', 'baklava', 'bamboo shoots', 'banana', 'barley', 'basil', 'bass', 'bay leaf', 'beancurd', 'beans', 'beef', 'beef carpaccio', 'beef steak', 'beef tartare', 'beet', 'beet salad', 'beignets', 'bell pepper', 'berry', 'bibimbap', 'bilberry', 'birthday cake', 'biscuits', 'bitter melon', 'black beans', 'black currant', 'blackberry', 'blood orange', 'blood sausage', 'blue cheese', 'blueberry', 'blueberry pie', 'bok choy', 'bonbon', 'boysenberry', 'bread', 'bread pudding', 'bread rolls', 'breadfruit', 'breadstick', 'bream', 'brie', 'brioche', 'brisket', 'brittle', 'broad beans', 'broccoli', 'broccolini', 'brown rice', 'brownie', 'brulee', 'bruschetta', 'brussels sprout', 'buckwheat', 'burrito', 'butter', 'cabbage', 'caesar salad', 'cake', 'cake pop', 'calamari', 'camembert', 'canape', 'candy', 'candy apple', 'candy bar', 'cannoli', 'cantaloupe', 'caper', 'caprese salad', 'caramel apple', 'cardoon', 'carp', 'carpaccio', 'carrot', 'carrot cake', 'cashew', 'cassava', 'casserole', 'cauliflower', 'caviar', 'celery', 'cereal', 'ceviche', 'chard', 'cheddar', 'cheese', 'cheeseburger', 'cheesecake', 'cherry', 'cherry tomato', 'chestnut', 'chicken', 'chicken breast', 'chicken curry', 'chicken leg', 'chicken wings', 'chickpeas', 'chili', 'chili pepper', 'chips', 'chives', 'chocolate', 'chorizo', 'chowder', 'churros', 'chutney', 'ciabatta', 'cinnamon roll', 'citron', 'citrus', 'clam', 'clam chowder', 'clementine', 'cobbler', 'cockle', 'coconut', 'coleslaw', 'collards', 'common bean', 'compote', 'cookie', 'corn', 'corn bread', 'corn salad', 'corned beef', 'cornflakes', 'cottage cheese', 'couscous', 'crab', 'crab cakes', 'cracker', 'cranberry', 'crayfish', 'creme brulee', 'crepe', 'crescent roll', 'cress', 'crispbread', 'croissant', 'croque madame', 'croquette', 'crouton', 'crunch', 'cucumber', 'cupcake', 'curd', 'currant', 'custard', 'cuttlefish', 'daikon', 'dandelion greens', 'danish pastry', 'date', 'deviled eggs', 'dough', 'doughnut', 'dragonfruit', 'dried apricot', 'dried fruit', 'drumstick', 'duck', 'dumpling', 'durian', 'eclair', 'edamame', 'eel', 'egg', 'egg white', 'egg yolk', 'eggplant', 'elderberry', 'endive', 'english muffin', 'escargots', 'falafel', 'farfalle', 'fava beans', 'fiddlehead', 'fig', 'filet mignon', 'fillet of sole', 'fish', 'fish and chips', 'flan', 'flatbread', 'flatfish', 'florence fennel', 'focaccia', 'foie gras', 'fondue', 'frankfurters', 'french beans', 'french bread', 'french fries', 'french onion soup', 'french toast', 'fried calamari', 'fried egg', 'fried rice', 'frittata', 'fritter', 'frozen yogurt', 'fruit salad', 'fruitcake', 'fudge', 'fusilli', 'galette', 'garlic', 'garlic bread', 'garlic chives', 'gazpacho', 'gherkin', 'ginger', 'gnocchi', 'goats cheese', 'goji berry', 'goose', 'gooseberry', 'gorgonzola', 'gouda', 'goulash', 'gourd', 'granola', 'grape', 'grapefruit', 'greek salad', 'green bean', 'green onion', 'grilled cheese sandwich', 'grits', 'ground beef', 'guacamole', 'guava', 'gyoza', 'gyro', 'habanero pepper', 'halibut', 'ham', 'hamburger', 'hash', 'hazelnut', 'herring', 'honey', 'honeydew melon', 'hot dog', 'huckleberry', 'huevos rancheros', 'hummus', 'ice cream', 'iceberg lettuce', 'jackfruit', 'jalapeno', 'jelly beans', 'jerusalem artichoke', 'jicama', 'jordan almonds', 'jujube', 'juniper berry', 'kale', 'kebab', 'kettle corn', 'kidney bean', 'kingfish', 'kipper', 'kiwi fruit', 'knish', 'kohlrabi', 'kombu', 'kumquat', 'lamb', 'lamb chops', 'lamb''s lettuce', 'lasagna', 'lavender', 'leek', 'lemon', 'lemon peel', 'lentil', 'lettuce', 'lima bean', 'lime', 'lobster', 'lobster bisque', 'loin', 'lollipop', 'lotus root', 'lox', 'lychee', 'macadamia nut', 'macaron', 'macaroni', 'macaroon', 'mackerel', 'mandarin orange', 'mango', 'maple syrup', 'marjoram', 'marshmallow', 'marzipan', 'mashed potatoes', 'meat', 'meat pie', 'meatball', 'meatloaf', 'melon', 'meringue', 'millet', 'mint', 'miso soup', 'mochi', 'mousse', 'mozzarella', 'muesli', 'muffin', 'mulberry', 'mung bean', 'mushroom', 'mussel', 'mutton', 'nachos', 'napa cabbage', 'nectarine', 'nigiri', 'noodle', 'nori', 'nougat', 'nut', 'oat', 'oatmeal', 'octopus', 'okra', 'olive', 'omelette', 'onion', 'onion rings', 'orange', 'oyster', 'pad thai', 'paella', 'pancake', 'pancetta', 'panna cotta', 'papaya', 'parfait', 'parmesan', 'parsnip', 'passionfruit', 'pasta', 'pastrami', 'pastry', 'pate', 'pea', 'peach', 'peanut', 'peapod', 'pear', 'pearl onion', 'pecan', 'penne', 'pepperoni', 'perch', 'persimmon', 'pho', 'pickle', 'pie', 'pike', 'pilaf', 'pine nut', 'pineapple', 'pistachio', 'pita bread', 'pizza', 'plum', 'polenta', 'pomegranate', 'pomelo', 'popcorn', 'popovers', 'poppy seed roll', 'popsicle', 'pork', 'pork chop', 'pork pie', 'porridge', 'pot roast', 'potato', 'potato onion', 'poutine', 'praline', 'prawn', 'pretzel', 'prime rib', 'prosciutto', 'prune', 'pudding', 'pumpkin', 'pumpkin seeds', 'quiche', 'quince', 'quinoa', 'radicchio', 'radish', 'raisin', 'raisin bread', 'rambutan', 'ramen', 'raspberry', 'ratatouille', 'ravioli', 'red cabbage', 'red velvet cake', 'rhubarb', 'ribbon-cut pasta', 'rice', 'risotto', 'roast beef', 'roe', 'romaine', 'roquefort', 'rosemary', 'rutabaga', 'sage', 'salad', 'salami', 'salmon', 'salsa', 'samosa', 'sandwich', 'sardine', 'sashimi', 'sauerkraut', 'sausage', 'sausage roll', 'scallion', 'scallop', 'scampi', 'scone', 'sea bass', 'seafood', 'seaweed salad', 'sesame seed', 'shallot', 'shellfish', 'sherbet', 'shish kebab', 'shortcake', 'shrimp', 'sirloin', 'slaw', 'smoked fish', 'smoked salmon', 'snapper', 'snow pea', 'soda bread', 'sorbet', 'sorghum', 'sorrel', 'souffle', 'soup', 'spaghetti bolognese', 'spaghetti carbonara', 'spare ribs', 'spinach', 'split peas', 'spring onion', 'spring rolls', 'sprinkles', 'sprouts', 'squash', 'squash blossoms', 'squid', 'star fruit', 'steak', 'stir-fry', 'strawberry', 'string bean', 'strudel', 'stuffing', 'sturgeon', 'succotash', 'summer squash', 'sundae', 'sunflower seeds', 'sushi', 'sweet potato', 'swiss chard', 'swiss cheese', 'tabouli', 'tacos', 'tagliatelle', 'tamale', 'tamarind', 'tangerine', 'tart', 'tartare', 'tempura', 'tenderloin', 'tiramisu', 'toast', 'toffee', 'tofu', 'tomatillo', 'tomato', 'torte', 'tortellini', 'tortilla chips', 'trout', 'truffle', 'tuna', 'tuna tartare', 'turkey', 'turkey breast', 'turnip', 'venison', 'vermicelli', 'wafer', 'waffle', 'walnut', 'water chestnut', 'watercress', 'watermelon', 'whipped cream', 'whoopie pie', 'winter melon', 'yam', 'yardlong bean', 'yellow summer squash', 'yogurt', 'zucchini']

class FoodAutocomplete(View):
    def get(self, request):
        query = request.GET.get('term', '')
        foods = Food.objects.filter(food_name__icontains=query)[:10]
        results = ["aaaaa","bbbbb","ccccc"]#[food.name for food in foods]
        return JsonResponse(results, safe=False)

from django.shortcuts import render
from .forms import ImageForm

import clarifai

def image_upload_view(request):
    """Process images uploaded by users"""
    #print("HEY")
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            #print("LOL")
            predict(img_obj.image.url)
            return render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
        else:
            form = ImageForm()
            return render(request, 'upload.html', {'form': form})
    else:
        form = ImageForm()
        return render(request, 'upload.html', {'form': form})
    
def predict(url):
    # Your PAT (Personal Access Token) can be found in the portal under Authentification
    PAT = 'c65c19a094404c88915f3889c8139bf3'
    # Specify the correct user_id/app_id pairings
    # Since you're making inferences outside your app's scope
    USER_ID = 'clarifai'
    APP_ID = 'main'
    # Change these to whatever model and image URL you want to use
    MODEL_ID = 'food-item-recognition'
    MODEL_VERSION_ID = '1d5fd481e0cf4826aa72ec3ff049e044'
    IMAGE_URL = url

    from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
    from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
    from clarifai_grpc.grpc.api.status import status_code_pb2

    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,  # The userDataObject is created in the overview and is required when using a PAT
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,  # This is optional. Defaults to the latest model version
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            url=IMAGE_URL
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    # Since we have one input, one output will exist here
    output = post_model_outputs_response.outputs[0]

    print("Predicted concepts:")
    for concept in output.data.concepts:
        print("%s %.2f" % (concept.name, concept.value))

    # Uncomment this line to print the full Response JSON
    print(output)