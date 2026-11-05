// The site's logo mark (same SVG as dist/logo.svg).
export function LogoMark(props: React.ComponentProps<'svg'>) {
  return (
    <svg viewBox="0 0 40 40" {...props}><rect x="1" y="1" width="38" height="38" rx="11" fill="#141413" /><path d="M12 13h16" stroke="#f1efea" strokeWidth="2.6" strokeLinecap="round" /><path d="M20 13v15" stroke="#f1efea" strokeWidth="2.6" strokeLinecap="round" /><path d="M20 28c0-6 3.5-9.5 9-9.5 0 6-3.5 9.5-9 9.5Z" fill="#f1efea" /></svg>
  )
}
