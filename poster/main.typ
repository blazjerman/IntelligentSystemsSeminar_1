#import "@preview/peace-of-posters:0.5.6" as pop

#set page("a0", margin: 1cm)
#pop.set-poster-layout(pop.layout-a0)

#show figure.caption: set text(size: .6em)

// Psevdo code stuff
#import "@preview/algorithmic:1.0.6"
#import algorithmic: style-algorithm, algorithm-figure, algorithm
#show: style-algorithm



#pop.set-theme(pop.uq)

#set text(size: pop.layout-a0.at("body-size"))
#let box-spacing = 1.2em
#set columns(gutter: box-spacing)
#set block(spacing: box-spacing)
#pop.update-poster-layout(spacing: box-spacing)

#pop.title-box("Nine men's morris (Mill)​",
  authors: "Blaž Jerman & Luka Matič​",
  institutes: "UP FAMNIT – PRIN",
  // keywords: "Peace, Dove, Poster, Science",
  logo: circle(image("famnit_logo.png", width: 100%), fill: white, inset: -10pt),
)

#columns(2,[

  #pop.column-box(heading: "Introduction")[
    
    - This project focuses on a two-player strategy game where the objective is to form mills and block the opponent’s moves. 
    - An AI agent was developed using adversarial search techniques to make optimal decisions. 
    
    - The system supports multiple difficulty levels and includes an option for human vs. AI gameplay, allowing players to compete against the algorithm interactively.​
    
  ]


#pop.column-box(heading: "Adversarial Search​")[
- The AI agent uses the Minimax algorithm with Alpha–Beta pruning to efficiently explore the game tree. 
- The evaluation function is defined as:


#show figure.where(kind: "algorithm"): set grid(column-gutter: .5em)

#algorithm-figure(
  "evaluation",
  indent: 0.9em,
  vstroke: 0.9pt + luma(100),
  {
    import algorithmic: *
    
    Function(
      "evaluation",
      ("game_state"),
      {

        Assign([player], [game_state.player])
        Assign([opponent], [game_state.opponent])

        
        Return[100 \* (player.pieces_c - opponent.pieces_c) + (player.moves_c - opponent.moves_c)]
      },
    )
  }
)



 

- Despite pruning, the search time grows rapidly beyond depth 5, limiting feasible depth in practice.

- When two optimal agents play against each other, the outcome is typically a draw, indicating balanced gameplay under perfect strategy.​




#figure(
  image("plot_minimax_no_pruning.png", width: 70%),
  caption: [Figure: This figure shows how the computation time of the Minimax algorithm increases exponentially with search depth—from 1.1 ms at depth 1 to over 200,000 ms at depth 5 and highlighting the need for pruning or depth limits in real-time play.​]
)


    

#figure(
  image("plot_minimax.png", width: 70%),
  caption: [This figure shows how the computation time of the Minimax algorithm increases exponentially with search depth—from 1.1 ms at depth 1 to over 67,000 ms at depth 7—highlighting the high computational cost of deeper searches and the need for optimization methods like alpha–beta pruning for real-time performance.]
)

  ]

#colbreak()
  
#pop.column-box(heading: "AI Difficulty Levels​")[
- The AI system supports three difficulty levels, defined by search depth: Easy (depth 1), Medium (depth 2), and Hard (depth 4). 

- Alternative approaches were also explored, including random move selection and distinct evaluation functions for each difficulty. 

- In tournament testing, the Hard agent consistently outperformed Medium and Easy, although most matches ended in draws due to the predefined turn limit.​



#align(center)[

  #figure(
    table(
    
    columns: 6,
    stroke: (x: .5pt),
    fill: luma(230),
  
      [Comparison], [Agent], [Wins], [Games Played], [Win Rate], [Draws],
      
      [Medium vs Easy], [Easy], [0], [20], [0.0%], [3],
      [Medium vs Hard], [Medium], [0], [20], [0.0%], [2], 
      [Easy vs Hard], [Easy], [0], [20], [0.0%], [2],
  
    
  ),


  caption: [AI difficulty comparison results table.
The table summarizes tournament outcomes between AI agents of different difficulty levels. Hard consistently beat Medium and Easy, with just a few draws (3 vs Medium, 2 vs Hard).]

  

)
]


    #figure(
      link("https://drive.google.com/file/d/1m8zl_3o0pYxmYC-37IkUmIyP-0eL37p7/view?usp=sharing", image("mill.png", width: 40%,)),  caption: [Without randomness, both agents fall into a repeating loop.]
    )

  ]
#pop.column-box(heading: "Human Interaction​")[
  
- In human–AI gameplay, the human player acts as Player 1, while the AI takes the role of Player 2. 

- Players make moves by clicking on legal positions on the board. 

- In testing, the Easy AI can be consistently beaten by human players, the Medium level offers a fair challenge, and the Hard level is rarely defeated, demonstrating the increasing strength of the AI with greater search depth.​






        #figure(
      link("https://drive.google.com/file/d/13-nd_6rc_byMHJpohQ90CevmbzjZ6FUw/view?usp=sharing", image("human_vs_ai.png", width: 40%)), caption: [The figure shows a player competing against the AI agent on the Nine Men’s Morris board. The AI responds to each move in real time, demonstrating its decision-making based on the Minimax algorithm with alpha–beta pruning.
]
    )

]


#pop.column-box(heading: "Results & Conclusions​")[
  
- Alpha–Beta pruning enables feasible real-time gameplay by significantly reducing the number of explored nodes.

- Difficulty scaling is achieved through a combination of search depth adjustment and controlled randomness in move selection. 
- The optimal AI agent never loses, ensuring strong defensive play. Human–AI interaction has proven engaging and competitive. 

- Future improvements include developing a more sophisticated evaluation function and implementing adaptive difficulty based on player performance.​
  ]

])


#pop.bottom-box()[
  #linebreak()
  GitHub implementation: #link("https://github.com/blazjerman/IntelligentSystemsSeminar_1")
]

//// ------------------


