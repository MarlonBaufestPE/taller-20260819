import { useNavigate } from 'react-router-dom'
import styles from './WelcomePage.module.css'

export default function WelcomePage() {
  const navigate = useNavigate()
  const username = sessionStorage.getItem('username') || 'Usuario'

  function handleLogout() {
    sessionStorage.removeItem('access_token')
    sessionStorage.removeItem('refresh_token')
    sessionStorage.removeItem('username')
    navigate('/login')
  }

  return (
    <div className={styles.page}>
      <nav className={styles.nav}>
        <div className={styles.navLogo}>
          <svg width="28" height="28" viewBox="0 0 32 32" fill="none" aria-hidden="true">
            <circle cx="16" cy="16" r="16" fill="#0070d1" />
            <path d="M10 22V10l8 4-8 8z" fill="white" />
          </svg>
          <span className={styles.navBrand}>PlayStation</span>
        </div>
        <button className={styles.logoutButton} onClick={handleLogout}>
          Cerrar sesión
        </button>
      </nav>

      <main className={styles.main}>
        <div className={styles.hero}>
          <p className={styles.eyebrow}>Bienvenido</p>
          <h1 className={styles.display}>{username}</h1>
          <p className={styles.body}>
            Has iniciado sesión correctamente. Explora tu experiencia PlayStation.
          </p>
          <button className={styles.ctaButton} onClick={handleLogout}>
            Cerrar sesión
          </button>
        </div>
      </main>
    </div>
  )
}
