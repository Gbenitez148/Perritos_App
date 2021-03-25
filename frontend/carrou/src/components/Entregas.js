import React from 'react'
import CardDeck from 'react-bootstrap/CardDeck'
import Card from 'react-bootstrap/Card'
import Container from 'react-bootstrap/Container'

function entregas() {
    return (
        <Container fluid className="mt-5" id="deck">
            <CardDeck>
              <Card>
                <Card.Img variant="top" src="https://holatelcel.com/wp-content/uploads/2018/07/HEAD-perrito-challenge.jpg" />
                <Card.Body>
                  <Card.Title>Titulo de la carta/nombre del perro</Card.Title>
                  <Card.Text>
                  Seña:
                  Vacunas:
                  Días nacido:
                  /Breve descripción del perro
                  </Card.Text>
                </Card.Body>
              </Card>
              <Card>
                <Card.Img variant="top" src="https://holatelcel.com/wp-content/uploads/2018/07/HEAD-perrito-challenge.jpg" />
                <Card.Body>
                  <Card.Title>Titulo de la carta/nombre del perro</Card.Title>
                  <Card.Text>
                  <p>Vacunas:
                    Antirrabica<br></br>
                    Seña: 1500$<br></br>
                    Días nacido:<br></br>
                    50 Días<br></br>
                    </p>
                 
                  </Card.Text>
                </Card.Body>
              </Card>
              <Card>
                <Card.Img variant="top" src="https://holatelcel.com/wp-content/uploads/2018/07/HEAD-perrito-challenge.jpg" />
                <Card.Body>
                  <Card.Title>Titulo de la carta/nombre del perro</Card.Title>
                  <Card.Text>
                  Seña:
                  Vacunas:
                  Días nacido:
                  /Breve descripción del perro
                  </Card.Text>
                </Card.Body>
                <Card.Footer>
                  <small className="text-muted">Last updated 3 mins ago</small>
                </Card.Footer>
              </Card>
              <h2 id= "Entregas"></h2>
            </CardDeck>
        </Container>
      
    )
}

export default entregas
