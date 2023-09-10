import pygame
import random

# Инициализация Pygame  # Pygame initialization
pygame.init()


# Определение цветов   # Defining colors
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
LIGHT_GREY = (200, 200, 200)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
DARK_GREEN = (0, 88, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Определение размеров экрана    # Determining screen sizes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Создание окна игры     # Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Blackjack")

# Загрузка изображений карт    # Load images
card_images = []

#Load card back
card_back = pygame.image.load(f'Cards/rewers.png')
dim_ratio = card_back.get_width()/card_back.get_height()
card_back = pygame.transform.scale(card_back, (dim_ratio*(SCREEN_HEIGHT//6), SCREEN_HEIGHT//6))
card_images.append(card_back)

#Load rest of cards
for suit in ("Clubs", "Diamonds", "Hearts", "Spades"):
    for i in range(1, 14):
        picture = pygame.image.load(f'Cards/{suit}/card{i}.png')
        dim_ratio = picture.get_width()/picture.get_height()		#WZ: zmienna pomocnicza, potrzebna do zachowania stosunu wymiarow kart przy skalowaniu
    
        picture = pygame.transform.scale(picture, (dim_ratio*(SCREEN_HEIGHT//6), SCREEN_HEIGHT//6))
        card_images.append(picture)


# Создание шрифтов    # Define font
font = pygame.font.SysFont('arial', 20)

# Определение размеров карты   # Card sizes
CARD_WIDTH = card_images[0].get_width()
CARD_HEIGHT = card_images[0].get_height()

# Определение размеров игровой области   # Play area size
GAME_AREA_WIDTH = SCREEN_WIDTH - 200
GAME_AREA_HEIGHT = SCREEN_HEIGHT - CARD_HEIGHT * 4

# Определение позиций игровых элементов    # Game elements positions
PLAYER_HAND_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40 - CARD_HEIGHT)
PLAYER_HAND_POSITION_1 = (SCREEN_WIDTH //2 - GAME_AREA_WIDTH//4, SCREEN_HEIGHT - 40 - CARD_HEIGHT)
PLAYER_HAND_POSITION_2 = (SCREEN_WIDTH //2 + GAME_AREA_WIDTH//4, SCREEN_HEIGHT - 40 - CARD_HEIGHT)
DEALER_HAND_POSITION = (SCREEN_WIDTH // 2, 40 + CARD_HEIGHT)
SCORE_POSITION = (SCREEN_WIDTH //2, SCREEN_HEIGHT - 55 - 1.5*CARD_HEIGHT)
SCORE_POSITION_1 = (SCREEN_WIDTH //2 - GAME_AREA_WIDTH//4, SCREEN_HEIGHT - 55 - 1.5*CARD_HEIGHT)	
SCORE_POSITION_2 = (SCREEN_WIDTH //2 + GAME_AREA_WIDTH//4, SCREEN_HEIGHT - 55 - 1.5*CARD_HEIGHT)				
DEALER_SCORE_POSITION = (SCREEN_WIDTH //2, 25 + CARD_HEIGHT//2)	
MESSAGE_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
MESSAGE_POSITION_1 = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)

BUTTON_HIT_POSITION = (60, SCREEN_HEIGHT - 40)
BUTTON_STAND_POSITION = (170, SCREEN_HEIGHT - 40)
BUTTON_SPLIT_POSITION = (280, SCREEN_HEIGHT - 40)
BUTTON_HIT_POSITION_1 = (SCREEN_WIDTH - 170, SCREEN_HEIGHT - 40)
BUTTON_STAND_POSITION_1 = (SCREEN_WIDTH - 60, SCREEN_HEIGHT - 40)

BUTTON_RESTART_POSITION = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40)
BUTTON_START_POSITION = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
BUTTON_EXIT_POSITION = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50)
BUTTON_MENU_POSITION = (SCREEN_WIDTH - 110, 50)


def define_sizes():
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    global GAME_AREA_WIDTH
    global GAME_AREA_HEIGHT
    global PLAYER_HAND_POSITION
    global DEALER_HAND_POSITION
    global SCORE_POSITION		
    global DEALER_SCORE_POSITION
    global MESSAGE_POSITION
    global BUTTON_HIT_POSITION 
    global BUTTON_STAND_POSITION
    global BUTTON_SPLIT_POSITION
    global BUTTON_RESTART_POSITION
    global BUTTON_START_POSITION
    global BUTTON_MENU_POSITION
    global BUTTON_EXIT_POSITION
    global SCORE_POSITION_1	
    global SCORE_POSITION_2
    global BUTTON_HIT_POSITION_1
    global BUTTON_STAND_POSITION_1
    global MESSAGE_POSITION_1
    global PLAYER_HAND_POSITION_1
    global PLAYER_HAND_POSITION_2

    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

    # Определение размеров игровой области   # Play area size
    GAME_AREA_WIDTH = SCREEN_WIDTH - 200
    GAME_AREA_HEIGHT = SCREEN_HEIGHT - CARD_HEIGHT * 4

    # Определение позиций игровых элементов    # Game elements positions
    PLAYER_HAND_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40 - CARD_HEIGHT)
    DEALER_HAND_POSITION = (SCREEN_WIDTH // 2, 40 + CARD_HEIGHT)
    SCORE_POSITION = (SCREEN_WIDTH //2, SCREEN_HEIGHT - 55 - 1.5*CARD_HEIGHT)			
    DEALER_SCORE_POSITION = (SCREEN_WIDTH //2, 25 + CARD_HEIGHT//2)	
    MESSAGE_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    BUTTON_HIT_POSITION = (60, SCREEN_HEIGHT - 40)
    BUTTON_STAND_POSITION = (170, SCREEN_HEIGHT - 40)
    BUTTON_SPLIT_POSITION = (280, SCREEN_HEIGHT - 40)
    BUTTON_RESTART_POSITION = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40)
    BUTTON_START_POSITION = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    BUTTON_MENU_POSITION = (SCREEN_WIDTH - 60, 30)
    BUTTON_EXIT_POSITION = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50)
    SCORE_POSITION_1 = (SCREEN_WIDTH //2 - GAME_AREA_WIDTH//4, SCREEN_HEIGHT - 55 - 1.5*CARD_HEIGHT)	
    SCORE_POSITION_2 = (SCREEN_WIDTH //2 + GAME_AREA_WIDTH//4, SCREEN_HEIGHT - 55 - 1.5*CARD_HEIGHT)	
    BUTTON_HIT_POSITION_1 = (SCREEN_WIDTH - 170, SCREEN_HEIGHT - 40)
    BUTTON_STAND_POSITION_1 = (SCREEN_WIDTH - 60, SCREEN_HEIGHT - 40)
    MESSAGE_POSITION_1 = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
    PLAYER_HAND_POSITION_1 = (SCREEN_WIDTH //2 - GAME_AREA_WIDTH//4, SCREEN_HEIGHT - 40 - CARD_HEIGHT)
    PLAYER_HAND_POSITION_2 = (SCREEN_WIDTH //2 + GAME_AREA_WIDTH//4, SCREEN_HEIGHT - 40 - CARD_HEIGHT)

# Определение значений карт    # Card values
CARD_VALUES = {
    'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10
}

CARD_SUIT = {'C': 0, 'D': 1, 'H': 2, 'S': 3}


# Dict for card-to-image conversion
CARD_TO_IMAGE = {
    'R': 0, 'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 11, 'Queen': 12, 'King': 13

}


def create_deck():
    #deck = list(CARD_VALUES.keys()) * 4
    deck = []
    
    for suit in list(CARD_SUIT.keys()):
        for value in list(CARD_VALUES.keys()):
            deck.append([suit, value])
    
    random.shuffle(deck)
    
    return deck


def deal_card(deck):
    return deck.pop()


def calculate_score(hand):
    score = sum(CARD_VALUES[ card[1] ] for card in hand)
    # Проверяем, есть ли на руках туз и нужно ли изменить его значение   # Logic for ace value
    for card in hand:
        if card[1] == 'Ace':
    	    if score > 21:
                score -= 10
                
    return score


def display_message(message, color, position):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(position[0], position[1]))
    screen.blit(text, text_rect)


def draw_card(card, position):
    screen.blit(card_images[ CARD_TO_IMAGE[card[1]] + CARD_SUIT[card[0]]*13 ], (position[0] - CARD_WIDTH // 2, position[1] - CARD_HEIGHT // 2))

# Рисует руку игрока или дилера    # Draws the player's or dealer's hand
def draw_hand(hand, position):
# Вычисляем смещение для центрирования карт    # Calculate offset to center maps
    offset = (len(hand) - 1) * CARD_WIDTH // 4
    # Рисуем каждую карту в руке    # Draw each card in hand
    for i, card in enumerate(hand):
        draw_card(card, (position[0] - offset + i * CARD_WIDTH // 2, position[1]))

# Рисует кнопку с текстом     # Draws a button with text
def draw_button(text, position, width=100, height=40):
    rect = pygame.Rect(position[0] - width/2, position[1] - height/2, width, height)
    pygame.draw.rect(screen, WHITE, rect, border_radius=10)

    text = font.render(text, True, BLACK)
    screen.blit(text, (position[0] - text.get_width() // 2, position[1] - text.get_height() // 2))
	
	#need Rect object for collidepoint
    return rect

# Modifies current bet
def modify_bet(bet, value, winnings):
    new_bet = bet
    
    if (bet + value) > winnings:
        new_bet = winnings
    elif (bet + value) < 10:
        new_bet = 10
    else:
        new_bet = bet + value
        
    return new_bet
    
def draw_betting_screen(bet, winnings):
    pygame.draw.rect(screen, BLACK, pygame.Rect(SCREEN_WIDTH//2 - 270, SCREEN_HEIGHT//2 - 70, 540, 155), border_radius=10)
    pygame.draw.rect(screen, LIGHT_GREY, pygame.Rect(SCREEN_WIDTH//2 - 266, SCREEN_HEIGHT//2 - 66, 532, 147), border_radius=10)

    rect_outer = pygame.Rect(SCREEN_WIDTH//2 - 60, SCREEN_HEIGHT//2 - 20, 120, 40)
    pygame.draw.rect(screen, BLACK, rect_outer, border_radius=10)
    
    rect_inner = pygame.Rect(SCREEN_WIDTH//2 - 58, SCREEN_HEIGHT//2 - 18, 116, 36)
    pygame.draw.rect(screen, WHITE, rect_inner, border_radius=10)
    
    display_message(f"Choose your bet:", BLACK, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 -  45))
    display_message(f"{bet}", BLACK, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    
    if bet <= 10:
        color_minus = GREY
    else:
        color_minus = WHITE
        
    if bet >= winnings:
        color_plus = GREY
    else:
        color_plus = WHITE
    
    button_minus_10 = pygame.Rect(SCREEN_WIDTH//2 - 125, SCREEN_HEIGHT//2 - 20, 60, 40)
    pygame.draw.rect(screen, color_minus, button_minus_10, border_radius=10)
    display_message("-10", BLACK, (SCREEN_WIDTH//2 - 95, SCREEN_HEIGHT//2))
    
    button_plus_10 = pygame.Rect(SCREEN_WIDTH//2 + 65, SCREEN_HEIGHT//2 - 20, 60, 40)
    pygame.draw.rect(screen, color_plus, button_plus_10, border_radius=10)
    display_message("+10", BLACK, (SCREEN_WIDTH//2 + 95, SCREEN_HEIGHT//2))
    
    button_minus_50 = pygame.Rect(SCREEN_WIDTH//2 - 190, SCREEN_HEIGHT//2 - 20, 60, 40)
    pygame.draw.rect(screen, color_minus, button_minus_50, border_radius=10)
    display_message("-50", BLACK, (SCREEN_WIDTH//2 - 160, SCREEN_HEIGHT//2))
    
    button_plus_50 = pygame.Rect(SCREEN_WIDTH//2 + 130, SCREEN_HEIGHT//2 - 20, 60, 40)
    pygame.draw.rect(screen, color_plus, button_plus_50, border_radius=10)
    display_message("+50", BLACK, (SCREEN_WIDTH//2 + 160, SCREEN_HEIGHT//2))
    
    button_minus_100 = pygame.Rect(SCREEN_WIDTH//2 - 255, SCREEN_HEIGHT//2 - 20, 60, 40)
    pygame.draw.rect(screen, color_minus, button_minus_100, border_radius=10)
    display_message("-100", BLACK, (SCREEN_WIDTH//2 - 225, SCREEN_HEIGHT//2))
    
    button_plus_100 = pygame.Rect(SCREEN_WIDTH//2 + 195, SCREEN_HEIGHT//2 - 20, 60, 40)
    pygame.draw.rect(screen, color_plus, button_plus_100, border_radius=10)
    display_message("+100", BLACK, (SCREEN_WIDTH//2 + 225, SCREEN_HEIGHT//2))
    
    return button_minus_100, button_minus_50, button_minus_10, button_plus_10, button_plus_50, button_plus_100     

# Func for drawing main menu screen
rands = []

def draw_menu():
    global rands
    offset = 5
    if len(rands) == 0:
        for i in range(22):
            rnum = random.randint(1, len(card_images)-1)
            rands.append(rnum)
    for i in range(11):
	    screen.blit(card_images[rands[i]], (SCREEN_WIDTH//2 - CARD_WIDTH // 2 + 25*offset, -CARD_HEIGHT // 2))
	    screen.blit(card_images[rands[i+5]], (SCREEN_WIDTH//2 - CARD_WIDTH // 2 - 25*offset, SCREEN_HEIGHT - CARD_HEIGHT // 2))
	    offset-=1

def main():
    menu = True
    running = True
    game_over = False
    adjust_winnings = False
    deck = create_deck()
    player_hand = []
    player_hand_1 = []
    player_hand_2 = []
    split_in_play = [0, 0]
    dealer_hand = []
    player_winnings = 500
    current_bet = 100
    player_score = 0
    player_score_1 = 0
    player_score_2 = 0
    dealer_score = 0
    show_message = 0
    betting_stage = True
    split_status = 0    # 0 - regular hand;  -1 - split refused;  1 - split possible; 2 - split taken 
    
    #WZ: dummy buttons - for collidepoint, proper coords set later
    hit_button = pygame.Rect(0, 0, 0, 0)
    stand_button = pygame.Rect(0, 0, 0, 0)
    hit_button_1 = pygame.Rect(0, 0, 0, 0)
    stand_button_1 = pygame.Rect(0, 0, 0, 0)
    res_button = pygame.Rect(0, 0, 0, 0)
    start_button = pygame.Rect(0, 0, 0, 0)
    split_button = pygame.Rect(0, 0, 0, 0)
    menu_button = pygame.Rect(0, 0, 0, 0)
    exit_button = pygame.Rect(0, 0, 0, 0)
    play_button = pygame.Rect(0, 0, 0, 0)
    
    # -100, -50, -10, 10, 50, 100
    bet_buttons = [pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)]
	
    while running:
        screen.fill(GREEN)
        define_sizes()
        
        if not menu:
            # Rectangle under dealer hand
            dealer_area = pygame.Rect( (SCREEN_WIDTH-GAME_AREA_WIDTH) // 2, 35 + CARD_HEIGHT//2, GAME_AREA_WIDTH, CARD_HEIGHT + 10)
            pygame.draw.rect(screen, DARK_GREEN, dealer_area, border_radius=5)
            # Rectangle under player hand
            player_area = pygame.Rect( (SCREEN_WIDTH-GAME_AREA_WIDTH) // 2, SCREEN_HEIGHT - 45 - 1.5*CARD_HEIGHT, GAME_AREA_WIDTH, CARD_HEIGHT + 10)
            pygame.draw.rect(screen, DARK_GREEN, player_area, border_radius=5) 
        
        # Обработка событий  # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Обработка нажатия кнопок     # Handling button presses
                if menu:
                    if start_button.collidepoint(event.pos):
                        menu = False
                        rands = []
                        game_over = False
                        deck = create_deck()
                        dealer_hand = []
                        player_hand = []
                        player_hand_1 = []
                        player_hand_2 = []
                        player_winnings = 500
                        current_bet = 100
                        player_score = 0
                        player_score_1 = 0
                        player_score_2 = 0
                        dealer_score = 0
                        betting_stage = True
                        adjust_winnings = False
                        show_message = 0
                        for _ in range(2):
                            player_hand.append(deal_card(deck))
                            dealer_hand.append(deal_card(deck))
                    elif exit_button.collidepoint(event.pos):
                        running = False
                elif betting_stage:
                    if player_winnings <= 0:
                        if menu_button.collidepoint(event.pos):
                            menu = True
                            
                        if start_button.collidepoint(event.pos):
                            menu = False
                            rands = []
                            game_over = False
                            deck = create_deck()
                            dealer_hand = []
                            player_hand = []
                            player_hand_1 = []
                            player_hand_2 = []
                            player_winnings = 500
                            current_bet = 100
                            player_score = 0
                            player_score_1 = 0
                            player_score_2 = 0
                            dealer_score = 0
                            betting_stage = True
                            adjust_winnings = False
                            show_message = 0
                            for _ in range(2):
                                player_hand.append(deal_card(deck))
                                dealer_hand.append(deal_card(deck))
                    
                    else:
                        if menu_button.collidepoint(event.pos):
                            menu = True
                        
                        elif play_button.collidepoint(event.pos):
                            betting_stage = False
                    
                        elif bet_buttons[0].collidepoint(event.pos):
                            current_bet = modify_bet(current_bet, -100, player_winnings)
                        
                        elif bet_buttons[1].collidepoint(event.pos):
                            current_bet = modify_bet(current_bet, -50, player_winnings)
                        
                        elif bet_buttons[2].collidepoint(event.pos):
                            current_bet = modify_bet(current_bet, -10, player_winnings)
                        
                        elif bet_buttons[3].collidepoint(event.pos):
                            current_bet = modify_bet(current_bet, 10, player_winnings)
                        
                        elif bet_buttons[4].collidepoint(event.pos):
                            current_bet = modify_bet(current_bet, 50, player_winnings)
                        
                        elif bet_buttons[5].collidepoint(event.pos):
                            current_bet = modify_bet(current_bet, 100, player_winnings)
                            
                elif not game_over and split_status < 2:
                    if hit_button.collidepoint(event.pos):		#need Rect object for collidepoint
                        player_hand.append(deal_card(deck))
                        player_score = calculate_score(player_hand)
                        if split_status == 1:
                            split_status == -1
                        
                        if player_score > 21:
                            dealer_score = calculate_score(dealer_hand)
                            show_message = 1	#"You went over 21. You lose!"
                            game_over = True
                            adjust_winnings = True
                            
                    elif stand_button.collidepoint(event.pos):
                        if split_status == 1:
                            split_status == -1
                        while dealer_score < 17:
                            dealer_hand.append(deal_card(deck))
                            dealer_score = calculate_score(dealer_hand)
                        if dealer_score > 21 or dealer_score < player_score:
                            show_message = 2	#"You win!"
                        elif dealer_score > player_score:
                            show_message = 3	#"You lose!"
                        else:
                            show_message = 4	#"It's a tie!"
                        game_over = True
                        adjust_winnings = True
                        
                    elif menu_button.collidepoint(event.pos):
                        menu = True
                        
                    elif split_button.collidepoint(event.pos) and split_status == 1:
                        split_status = 2
                        player_hand_1.append(player_hand[0])
                        player_hand_2.append(player_hand[1])
                        player_hand_1.append(deal_card(deck))
                        player_hand_2.append(deal_card(deck))
                        split_in_play = [1, 1]
                        player_hand = []
                
                
                # Hand was split       
                elif not game_over and split_status == 2:
                    if hit_button.collidepoint(event.pos) and split_in_play[0]:		#need Rect object for collidepoint
                        player_hand_1.append(deal_card(deck))
                        player_score_1 = calculate_score(player_hand_1)
                        if player_score_1 > 21:
                            split_in_play[0] = 0
                            if not split_in_play[0] and not split_in_play[1]:
                                dealer_score = calculate_score(dealer_hand)
                                show_message = 5
                                game_over = True
                                adjust_winnings = True
                    
                    elif hit_button_1.collidepoint(event.pos) and split_in_play[1]:		#need Rect object for collidepoint
                        player_hand_2.append(deal_card(deck))
                        player_score_2 = calculate_score(player_hand_2)
                        if player_score_2 > 21:
                            split_in_play[1] = 0
                            if not split_in_play[0] and not split_in_play[1]:
                                dealer_score = calculate_score(dealer_hand)
                                show_message = 5
                                game_over = True
                                adjust_winnings = True
                            
                    elif stand_button.collidepoint(event.pos):
                        split_in_play[0] = 0
                        
                        if not split_in_play[0] and not split_in_play[1]:
                            while dealer_score < 17:
                                dealer_hand.append(deal_card(deck))
                                dealer_score = calculate_score(dealer_hand)
                            
                            show_message = 5
                            game_over = True
                            adjust_winnings = True
                            
                    elif stand_button_1.collidepoint(event.pos):
                        split_in_play[1] = 0
                        
                        if not split_in_play[0] and not split_in_play[1]:
                            while dealer_score < 17:
                                dealer_hand.append(deal_card(deck))
                                dealer_score = calculate_score(dealer_hand)
                            
                            show_message = 5
                            game_over = True
                            adjust_winnings = True
                        
                    elif menu_button.collidepoint(event.pos):
                        menu = True
                            
                else:
                    if res_button.collidepoint(event.pos):
                        # Начать новую игру    # Start a new game
                        game_over = False
                        deck = create_deck()
                        dealer_hand = []
                        player_hand = []
                        player_hand_1 = []
                        player_hand_2 = []
                        player_score = 0
                        player_score_1 = 0
                        player_score_2 = 0
                        dealer_score = 0
                        show_message = 0
                        split_status = 0
                        betting_stage = True
                        adjust_winnings = False
                        
                        for _ in range(2):
                            player_hand.append(deal_card(deck))
                            dealer_hand.append(deal_card(deck))
                    elif menu_button.collidepoint(event.pos):
                        menu = True

        # Обновление экрана    # Screen refresh
        if menu:
            draw_menu()
            start_button = draw_button("START", BUTTON_START_POSITION)
            exit_button = draw_button("Exit", BUTTON_EXIT_POSITION)
            
        elif betting_stage:
            if player_winnings <= 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2 - 70, 300, 120), border_radius=10)
                pygame.draw.rect(screen, LIGHT_GREY, pygame.Rect(SCREEN_WIDTH//2 - 146, SCREEN_HEIGHT//2 - 66, 292, 112), border_radius=10)
                display_message(f"You ran out of money. You lose!", BLACK, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
                display_message(f"Start a new game?", BLACK, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 20))
                menu_button = draw_button("Menu", (SCREEN_WIDTH//2 + 55, SCREEN_HEIGHT//2 + 20))
                start_button = draw_button("New Game", (SCREEN_WIDTH//2 - 55, SCREEN_HEIGHT//2 + 20))
                
            else:
                screen.blit( font.render(f"Winnings: ${player_winnings}", True, BLACK), (10, 10))
                bet_buttons[0], bet_buttons[1], bet_buttons[2], bet_buttons[3], bet_buttons[4], bet_buttons[5] = draw_betting_screen(current_bet, player_winnings)
                menu_button = draw_button("Menu", BUTTON_MENU_POSITION)
                play_button = draw_button("Play!", (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
            
        elif not game_over:
            if split_status < 2:
                hit_button = draw_button("Hit", BUTTON_HIT_POSITION)
                stand_button = draw_button("Stand", BUTTON_STAND_POSITION)
                player_score = calculate_score(player_hand)
                display_message(f"Player's Score: {player_score}", BLACK, SCORE_POSITION)
                draw_hand(player_hand, PLAYER_HAND_POSITION)
            else:
                player_score_1 = calculate_score(player_hand_1)
                player_score_2 = calculate_score(player_hand_2)
                display_message(f"Left Score: {player_score_1}", BLACK, SCORE_POSITION_1)
                draw_hand(player_hand_1, PLAYER_HAND_POSITION_1)
                display_message(f"Right Score: {player_score_2}", BLACK, SCORE_POSITION_2)
                draw_hand(player_hand_2, PLAYER_HAND_POSITION_2)
                
                if split_in_play[0]:
                    hit_button = draw_button("Hit", BUTTON_HIT_POSITION)
                    stand_button = draw_button("Stand", BUTTON_STAND_POSITION)
                if split_in_play[1]:
                    hit_button_1 = draw_button("Hit", BUTTON_HIT_POSITION_1)
                    stand_button_1 = draw_button("Stand", BUTTON_STAND_POSITION_1)
                    
            draw_hand( (dealer_hand[0], ['C', 'R'] ), DEALER_HAND_POSITION)
            dealer_score = calculate_score( [dealer_hand[0]] )  # Показываем только вторую карту дилера   # Show score only for revealed card
            display_message(f"Dealer's Score: {dealer_score}", BLACK, DEALER_SCORE_POSITION)
            screen.blit( font.render(f"Winnings: ${player_winnings}", True, BLACK), (10, 10))
            screen.blit( font.render(f"Current bet: ${current_bet}", True, BLACK), (10, 40))
            menu_button = draw_button("Menu", BUTTON_MENU_POSITION)
            
            if len(player_hand) == 2 and player_hand[0][1] == player_hand[1][1] and split_status != 2 and split_status != -1:
                split_button = draw_button("Split", BUTTON_SPLIT_POSITION)
                split_status = 1
                
        else:
            if adjust_winnings:
                if show_message == 1:
                    player_winnings -= current_bet
                elif show_message == 2:
                    player_winnings += current_bet
                elif show_message == 3:
                    player_winnings -= current_bet
                elif show_message == 5:
                    if (player_score_1 <= 21 and player_score_1 > dealer_score):
                        player_winnings += current_bet
                    elif player_score_1 > 21 or player_score_1 < dealer_score:
                        player_winnings -= current_bet
                        
                    if (player_score_2 <= 21 and player_score_2 > dealer_score):
                        player_winnings += current_bet
                    elif player_score_2 > 21 or player_score_2 < dealer_score:
                        player_winnings -= current_bet
                
                adjust_winnings = False
        
            if split_status < 2:
                draw_hand(player_hand, PLAYER_HAND_POSITION)
                display_message(f"Player's Score: {player_score}", BLACK, SCORE_POSITION)
                
            else:
                display_message(f"Left Score: {player_score_1}", BLACK, SCORE_POSITION_1)
                draw_hand(player_hand_1, PLAYER_HAND_POSITION_1)
                display_message(f"Right Score: {player_score_2}", BLACK, SCORE_POSITION_2)
                draw_hand(player_hand_2, PLAYER_HAND_POSITION_2)
                    
            draw_hand(dealer_hand, DEALER_HAND_POSITION)
            display_message(f"Dealer's Score: {dealer_score}", BLACK, DEALER_SCORE_POSITION)     
            res_button = draw_button("Next Round", BUTTON_RESTART_POSITION, width = 120)
            menu_button = draw_button("Menu", BUTTON_MENU_POSITION)
            
            #Redrawing messages
            if show_message == 1:
                display_message("You went over 21. You lose!", RED, MESSAGE_POSITION)
            elif show_message == 2:
                display_message("You win!", BLUE, MESSAGE_POSITION)
            elif show_message == 3:
                display_message("You lose!", RED, MESSAGE_POSITION)
            elif show_message == 4:
                display_message("It's a tie!", BLACK, MESSAGE_POSITION)
            elif show_message == 5:
                if player_score_1 <= 21 and player_score_1 > dealer_score:
                    display_message("Left hand wins!", BLUE, MESSAGE_POSITION_1)
                elif player_score_1 <= 21 and player_score_1 == dealer_score:
                    display_message("Left hand ties.", BLACK, MESSAGE_POSITION_1)
                elif player_score_1 <= 21 and player_score_1 < dealer_score:
                    display_message("Left hand loses.", RED, MESSAGE_POSITION_1)
                else:
                    display_message("Left hand went over 21.", RED, MESSAGE_POSITION_1)
                       
                if player_score_2 <= 21 and player_score_2 > dealer_score:
                    display_message("Right hand wins!", BLUE, MESSAGE_POSITION)
                elif player_score_2 <= 21 and player_score_2 == dealer_score:
                    display_message("Right hand ties.", BLACK, MESSAGE_POSITION)
                elif player_score_2 <= 21 and player_score_2 < dealer_score:
                    display_message("Right hand loses.", RED, MESSAGE_POSITION)
                else:
                    display_message("Right hand went over 21.", RED, MESSAGE_POSITION)
                

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    
    
    
    
    
