import { useNavigate } from 'react-router-dom'
import styles from './WelcomePage.module.css'

const aiCertifications = [
  {
    name: 'Machine Learning Operations Engineer Associate',
    description:
      'Reemplaza a Azure Data Scientist Associate. Valida habilidades para operacionalizar, monitorear y mantener modelos de machine learning en producción.',
  },
  {
    name: 'Azure AI Apps and Agents Developer Associate',
    description:
      'Reemplaza a Azure AI Engineer Associate. Certifica el desarrollo de aplicaciones y agentes de IA generativa sobre Azure AI Foundry.',
  },
  {
    name: 'Agentic AI Business Solutions Architect',
    description:
      'Nueva certificación experta que valida el diseño de soluciones de negocio impulsadas por agentes de IA sobre Dynamics 365 y Power Platform.',
  },
  {
    name: 'Azure Databricks Data Engineer Associate',
    description:
      'Nueva certificación que valida habilidades de ingeniería de datos e IA a gran escala utilizando Azure Databricks.',
  },
  {
    name: 'SQL AI Developer Associate',
    description:
      'Nueva certificación enfocada en construir soluciones inteligentes que integran IA con bases de datos SQL.',
  },
]

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

        <section className={styles.certSection}>
          <p className={styles.eyebrow}>Novedades 2026</p>
          <h2 className={styles.certHeading}>Nuevas certificaciones de Microsoft en Inteligencia Artificial</h2>
          <div className={styles.certGrid}>
            {aiCertifications.map(cert => (
              <article className={styles.certCard} key={cert.name}>
                <h3 className={styles.certCardTitle}>{cert.name}</h3>
                <p className={styles.certCardBody}>{cert.description}</p>
              </article>
            ))}
          </div>
        </section>
      </main>
    </div>
  )
}
