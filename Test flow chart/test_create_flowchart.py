import graphviz

# Use the specified path when rendering the flowchart
flowchart = graphviz.Digraph('flowchart')

# Define nodes (shapes) and edges (arrows)
flowchart.node('A', 'Start')
flowchart.node('B', 'Choose Test Mode')
flowchart.node('C', 'Get Current Timestamp')
flowchart.node('D', 'Power Cycle Test')
flowchart.node('E', 'Turn PoE Off')
flowchart.node('F', 'Check PoE Status')
flowchart.node('G', 'Turn PoE On')
flowchart.node('H', 'Check PoE Status')
flowchart.node('I', 'Initialize Camera')
flowchart.node('J', 'Get Device Info')
flowchart.node('K', 'Start Image Grabbing')
flowchart.node('L', 'Retrieve Image Result')
flowchart.node('M', 'Check Grab Success')
flowchart.node('N', 'Release Resources')
flowchart.node('O', 'Check Test Result')
flowchart.node('P', 'Increment Test Iteration')
flowchart.node('Q', 'Check Test Iteration Limit')
flowchart.node('R', 'End')

flowchart.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI', 'IJ', 'JK', 'KL', 'LM', 'MN', 'NO', 'OP', 'PQ', 'QR'])

# Save the flowchart as an image file
flowchart.render(filename='Test flow chart\flowchart', format='png')
