from dataclasses import dataclass


@dataclass
class Tunnel:
    name: str = ''
    t: str = ''
    lvl: str = ''
    msg: str = ''
    obj: str = ''
    addr: str = ''
    url: str = ''


def tunnel_toHTML(tunnels):
    html = ''
    html += headerHTML()
    html += tunnelsHTML(tunnels)
    html += footerHTML()
    return html


def tunnelsHTML(tunnels):
    i = 0
    html = ''
    for tn_name, tn in tunnels.items():
        i += 1
        html += f'''
            <tr>
              <th scope="row">{i}</th>
              <td>{tn_name}</td>
              <td><a rel="noopener noreferrer" target="_blank"
                   href="{tn.url}">{tn.url}</a>
              </td>
              <td>{tn.addr}</td>
              <td>{tn.t}</td>
            </tr>
        '''
    return html


def headerHTML():
    return '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Active Tunnels</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="#">Navbar</a>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item"><a class="nav-link active" aria-current="page" href="#">Home</a></li>
            <li class="nav-item"><a class="nav-link" href="#">Link</a></li>
            <li class="nav-item"><a class="nav-link disabled">Disabled</a></li>
          </ul>
          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>

    <div class="container my-5">
      <table class="table table-hover">
        <thead class="thead-dark">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">URL</th>
            <th scope="col">Local URL</th>
            <th scope="col">Created</th>
          </tr>
        </thead>
        <tbody>
    '''


def footerHTML():
    return '''
        </tbody></table>
    </div></body>
</html>
    '''