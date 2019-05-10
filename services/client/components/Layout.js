import Header from './Header'
import Sidebar from './Sidebar'
import Content from './Content'
import Footer from './Footer'


const Layout = props => (
  <div>
    <Header />
    <Content>
    {props.children}
    </Content>
    <Sidebar />
    <Footer />
  </div>
)

export default Layout