class Card_Imgs:
    # f"┌───────────────┐",
    # f"│ 10 ♥     ♥    │",
    # f"│       ♥       │",
    # f"│    ♥     ♥    │",
    # f"│               │",
    # f"│               │",
    # f"│               │",
    # f"│    ♥     ♥    │",
    # f"│       ♥       │",
    # f"│    ♥     ♥ 10 │",
    # f"└───────────────┘"

    def return_card(suit, rank):
        cardColor = "\033[37m"
        ENDC = '\033[0m'

        if suit == "Hearts":
            suit = "♥"
        elif suit == "Spades":
            suit = "♠"
        elif suit == "Diamonds":
            suit = "♦"
        elif suit == "Clubs":
            suit = "♣"

        ace = [
            f"┌───────────────┐",
            f"│ A             │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│       {cardColor}{suit}{ENDC}       │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│             A │",
            f"└───────────────┘"
        ]

        two = [
            f"┌───────────────┐",
            f"│ 2     {cardColor}{suit}{ENDC}       │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│       {cardColor}{suit}{ENDC}    2  │",
            f"└───────────────┘"
        ]

        three = [
            f"┌───────────────┐",
            f"│ 3     {cardColor}{suit}{ENDC}       │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│       {cardColor}{suit}{ENDC}       │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│       {cardColor}{suit}{ENDC}     3 │",
            f"└───────────────┘"
        ]

        four = [
            f"┌───────────────┐",
            f"│ 4  {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}  4 │",
            f"└───────────────┘"
        ]

        five = [
            f"┌───────────────┐",
            f"│ 5  {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│       {cardColor}{suit}{ENDC}       │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}  5 │",
            f"└───────────────┘"
        ]

        six = [
            f"┌───────────────┐",
            f"│ 6  {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}  6 │",
            f"└───────────────┘"
        ]

        seven = [
            f"┌───────────────┐",
            f"│ 7  {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│       {cardColor}{suit}{ENDC}       │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}  7 │",
            f"└───────────────┘"
        ]

        eight = [
            f"┌───────────────┐",
            f"│ 8  {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}  8 │",
            f"└───────────────┘"
        ]

        nine = [
            f"┌───────────────┐",
            f"│ 9  {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│       {cardColor}{suit}{ENDC}       │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}  9 │",
            f"└───────────────┘"
        ]

        ten = [
            f"┌───────────────┐",
            f"│ 10 {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│       {cardColor}{suit}{ENDC}       │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│               │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│       {cardColor}{suit}{ENDC}       │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC} 10 │",
            f"└───────────────┘"
        ]

        jack = [
            f"┌───────────────┐",
            f"│ J             │",
            f"│               │",
            f"│     {cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}    │",
            f"│        {cardColor}{suit}{ENDC}      │",
            f"│        {cardColor}{suit}{ENDC}      │",
            f"│    {cardColor}{suit}{ENDC}   {cardColor}{suit}{ENDC}      │",
            f"│     {cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}       │",
            f"│               │",
            f"│             J │",
            f"└───────────────┘"
        ]

        queen = [
            f"┌───────────────┐",
            f"│ Q             │",
            f"│     {cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}      │",
            f"│    {cardColor}{suit}{ENDC}    {cardColor}{suit}{ENDC}     │",
            f"│   {cardColor}{suit}{ENDC}      {cardColor}{suit}{ENDC}    │",
            f"│   {cardColor}{suit}{ENDC}      {cardColor}{suit}{ENDC}    │",
            f"│    {cardColor}{suit}{ENDC}  {cardColor}{suit}{ENDC} {cardColor}{suit}{ENDC}     │",
            f"│     {cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}{cardColor}{suit}{ENDC}      │",
            f"│          {cardColor}{suit}{ENDC}    │",
            f"│             Q │",
            f"└───────────────┘"
        ]

        king = [
            f"┌───────────────┐",
            f"│ K             │",
            f"│               │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│    {cardColor}{suit}{ENDC}   {cardColor}{suit}{ENDC}      │",
            f"│    {cardColor}{suit}{ENDC} {cardColor}{suit}{ENDC}        │",
            f"│    {cardColor}{suit}{ENDC}   {cardColor}{suit}{ENDC}      │",
            f"│    {cardColor}{suit}{ENDC}     {cardColor}{suit}{ENDC}    │",
            f"│               │",
            f"│             K │",
            f"└───────────────┘"
        ]

        dictionary = {"2": two, "3": three, "4": four, "5": five, "6": six, "7": seven, 
                       "8": eight, "9": nine, "10": ten, "11": jack, "12": queen, "13": king, "14": ace}
        
        return dictionary[str(rank)]
