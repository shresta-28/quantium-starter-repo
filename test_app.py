from app import app

def test_header(dash_duo):
    dash_duo.start_server(app)
    header_element = dash_duo.find_element("#header")
    assert header_element is not None

def test_visualized(dash_duo):
    dash_duo.start_server(app)
    graph_element = dash_duo.find_element("#sales-line-chart")
    assert graph_element is not None

def test_radio(dash_duo):
    dash_duo.start_server(app)
    radio_element = dash_duo.find_element("#region-radio")
    assert radio_element is not None