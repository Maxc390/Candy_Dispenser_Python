import pygame
import sys

#import Button class
from custom_button import Button

#import Node and Stack classes
from custom_stackclass import Node, Stack
# Initialize pygame
pygame.init()

# Constant parameters
WIDTH, HEIGHT = 850, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stack Illustration")

# Fonts
font = pygame.font.Font(None, 36)

# Load spring image
spring_img = pygame.image.load('spring3.png')
spring_img = pygame.transform.scale(spring_img, (150, 50))

# Entry box
input_text = ""
input_rect = pygame.Rect(580, HEIGHT - 450, 140, 40)
font = pygame.font.Font(None, 32)

#creating variable to display messages
top_message = None
is_empty_message = None
length_message = None

#create stack
stack = Stack()


# Creating buttons
push_button = Button(580, 200, 115, 40, "Push", "push")
pop_button = Button(580, 250, 115, 40, "Pop", "pop")
top_button = Button(580, 300, 115, 40, "Top", "top")
len_button = Button(710, 200, 115, 40, "Length", "length")
is_empty_button = Button(710, 250, 115, 40, "Is_Empty", "is_empty")
Quit_button = Button(710,300,115,40,"Quit","quit")

# Game Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #defining how the entrybox works
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            #only integer values are accepted and enter button pushes into stack as the default function.
            elif event.key == pygame.K_RETURN:
                if input_text.isnumeric():
                    stack.push(int(input_text))
                input_text = ""
            else:
                input_text += event.unicode
        
        #checking and defining what happens if buttons are clicked.

        if event.type == pygame.MOUSEBUTTONDOWN:
            #Get mouse position
            pos = pygame.mouse.get_pos()
            #Push
            if push_button.is_clicked(pos) and input_text.isnumeric():
                stack.push(int(input_text))
                input_text = ""
            #pop
            elif pop_button.is_clicked(pos):
                stack.pop()
            #Top
            elif top_button.is_clicked(pos):
                top_value = stack.peek()
                print("Top:", top_value)  # You can use this value as needed
                top_message = f"Top: {top_value}" if top_value is not None else "Stack is empty"
            #Length of stack
            elif len_button.is_clicked(pos):
                length = stack.length()
                print("Length:", length)  # You can use this value as needed
                length_message = f"Length: {length}"
            #Is stack empty?
            elif is_empty_button.is_clicked(pos):
                is_empty = stack.is_empty()
                print("Is Empty:", is_empty)  # You can use this value as needed
                is_empty_message = "Stack is empty" if is_empty else "Stack is not empty"
            #Quit button to quit game
            elif Quit_button.is_clicked(pos):
                running = False

            # Reset button click state after mouse clicked
            push_button.clicked = False
            pop_button.clicked = False
            top_button.clicked = False
            len_button.clicked = False
            is_empty_button.clicked = False
            Quit_button.clicked = False

    # Clear the screen
    screen.fill(WHITE)

    # Drawing the stack container
    pygame.draw.rect(screen, BLUE, (20, 20, 200, HEIGHT - 40))

    #spring parameters definition
    spring_x = 40
    spring_bottom_y = HEIGHT - 75  # Constant bottom Y-coordinate
    spring_height = 50  # Initial spring height
    spring_img = pygame.transform.scale(spring_img, (150, spring_height))

    # Calculate the initial top Y-coordinate based on the spring height
    spring_top_y = spring_bottom_y - spring_height

    # Draw stack elements in reverse order
    current_node = stack.top_node
    items = []  # Store the items in a list

    #set next node as the top node
    while current_node:
        items.append(current_node.data)
        current_node = current_node.next

    # Reverse the list to draw the items from the bottom to the top
    items.reverse()

    #Drawing each object into the container with its custom text.

    for i, item in enumerate(items):
        # Calculate the Y-coordinate for the candy ellipse
        candy_y = HEIGHT - 110 - i * 40

        # Draw the candy ellipse
        pygame.draw.ellipse(screen, RED, (40, candy_y, 160, 30))

        # Draw the text on the candy ellipse
        text = font.render(str(item), True, WHITE)
        screen.blit(text, (100, candy_y + 8))

        # Calculate the Y-coordinate for the spring's center
        spring_center_y = (spring_bottom_y + spring_top_y) // 2
        spring_center_y += 1  # Move the spring's center down by 1 pixel for each item

        # Adjusting the spring top and bottom Y-coordinates proportionally
        spring_top_y = spring_center_y - spring_height // 2
        spring_bottom_y = spring_center_y + spring_height // 2

        # Update the spring image's scale based on the new height
        spring_img = pygame.transform.scale(spring_img, (150, spring_height))



    # Drawing the spring at the container's bottom
    screen.blit(spring_img, (spring_x, spring_bottom_y))

    # Drawing the entry box
    pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)
    text_surface = font.render(input_text, True, (0, 0, 0))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(200, text_surface.get_width() + 10)

    # Drawing the buttons
    push_button.draw(screen)
    pop_button.draw(screen)
    top_button.draw(screen)
    len_button.draw(screen)
    is_empty_button.draw(screen)
    Quit_button.draw(screen)

    # Blit the message surfaces to window
    if top_message:
        top_text_surface = font.render(top_message, True, (0, 0, 0))
        screen.blit(top_text_surface, (250, 400))
    if length_message:
        length_text_surface = font.render(length_message, True, (0, 0, 0))
        screen.blit(length_text_surface, (250, 440))
    if is_empty_message:
        is_empty_text_surface = font.render(is_empty_message, True, (0, 0, 0))
        screen.blit(is_empty_text_surface, (250, 480))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()

