'use client'; // Ensure this file uses client-side rendering

import { useEffect } from 'react';
import styled, { createGlobalStyle } from 'styled-components';
import gsap from 'gsap';

const GsapComponent = () => {
  useEffect(() => {
    const UPDATE = ({ x, y }) => {
      gsap.to(document.documentElement, {
        '--x': gsap.utils.mapRange(0, window.innerWidth, -0.45, 0.45, x), // Adjusted range
        '--y': gsap.utils.mapRange(0, window.innerHeight, -0.45, 0.45, y), // Adjusted range
        duration: 0.5, // Smoother transition
        ease: 'power2.out' // Natural easing
      });
    };

    const handleMouseMove = (event) => {
      UPDATE({ x: event.clientX, y: event.clientY });
    };

    const handleTouchMove = (event) => {
      if (event.touches.length > 0) {
        const touch = event.touches[0];
        UPDATE({ x: touch.clientX, y: touch.clientY });
      }
    };

    const handleOrientation = (event) => {
      const { beta, gamma } = event;
      const isLandscape = window.matchMedia('(orientation: landscape)').matches;
      gsap.to(document.documentElement, {
        '--x': gsap.utils.clamp(
          -0.2,
          0.2,
          isLandscape
            ? gsap.utils.mapRange(-45, 45, -0.2, 0.2, beta)
            : gsap.utils.mapRange(-45, 45, -0.2, 0.2, gamma)
        ),
        '--y': gsap.utils.clamp(
          -0.2,
          0.2,
          isLandscape
            ? gsap.utils.mapRange(20, 70, 0.2, -0.2, Math.abs(gamma))
            : gsap.utils.mapRange(20, 70, 0.2, -0.2, beta)
        ),
        duration: 0.5, // Smoother transition
        ease: 'power2.out' // Natural easing
      });
    };

    const START = () => {
      if (DeviceOrientationEvent && typeof DeviceOrientationEvent.requestPermission === 'function') {
        DeviceOrientationEvent.requestPermission()
          .then(permissionState => {
            if (permissionState === 'granted') {
              window.addEventListener('deviceorientation', handleOrientation);
            }
          })
          .catch(console.error);
      } else {
        window.addEventListener('deviceorientation', handleOrientation);
      }
    };

    window.addEventListener('mousemove', handleMouseMove);
    window.addEventListener('touchmove', handleTouchMove);
    document.body.addEventListener('click', START, { once: true });

    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('touchmove', handleTouchMove);
      window.removeEventListener('deviceorientation', handleOrientation);
      document.body.removeEventListener('click', START);
    };
  }, []);

  return (
    <>
      <GlobalStyle />
      <Main>
        <LinkWrapper
          href="https://twitter.com/intent/follow?screen_name=jh3yy"
          target="_blank"
          rel="noreferrer noopener"
        >
          <svg
            className="w-9"
            viewBox="0 0 969 955"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <circle cx="161.191" cy="320.191" r="133.191" stroke="currentColor" strokeWidth="20" />
            <circle cx="806.809" cy="320.191" r="133.191" stroke="currentColor" strokeWidth="20" />
            <circle cx="695.019" cy="587.733" r="31.4016" fill="currentColor" />
            <circle cx="272.981" cy="587.733" r="31.4016" fill="currentColor" />
            <path
              d="M564.388 712.083C564.388 743.994 526.035 779.911 483.372 779.911C440.709 779.911 402.356 743.994 402.356 712.083C402.356 680.173 440.709 664.353 483.372 664.353C526.035 664.353 564.388 680.173 564.388 712.083Z"
              fill="currentColor"
            />
            <rect x="310.42" y="448.31" width="343.468" height="51.4986" fill="#FF1E1E" />
            <path
              fillRule="evenodd"
              clipRule="evenodd"
              d="M745.643 288.24C815.368 344.185 854.539 432.623 854.539 511.741H614.938V454.652C614.938 433.113 597.477 415.652 575.938 415.652H388.37C366.831 415.652 349.37 433.113 349.37 454.652V511.741L110.949 511.741C110.949 432.623 150.12 344.185 219.845 288.24C289.57 232.295 384.138 200.865 482.744 200.865C581.35 200.865 675.918 232.295 745.643 288.24Z"
              fill="currentColor"
            />
          </svg>
        </LinkWrapper>
        <ArticleWrapper>
          <Assets>
            <img src="https://assets.codepen.io/605876/osaka-sky.jpeg" alt="Osaka Sky" />
            <h3>Osaka</h3>
            <img src="https://assets.codepen.io/605876/osaka-tower.png" alt="Osaka Tower" />
          </Assets>
          <Blur>
            <div>
              <div className="layer" style={{ '--index': 1 }}></div>
              <div className="layer" style={{ '--index': 2 }}></div>
              <div className="layer" style={{ '--index': 3 }}></div>
              <div className="layer" style={{ '--index': 4 }}></div>
              <div className="layer" style={{ '--index': 5 }}></div>
            </div>
          </Blur>
          <Content>
            <p>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="currentColor"
                className="w-6 h-6"
              >
                <path d="M15.75 8.25a.75.75 0 0 1 .75.75c0 1.12-.492 2.126-1.27 2.812a.75.75 0 1 1-.992-1.124A2.243 2.243 0 0 0 15 9a.75.75 0 0 1 .75-.75Z" />
                <path
                  fillRule="evenodd"
                  clipRule="evenodd"
                  d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25ZM4.575 15.6a8.25 8.25 0 0 0 9.348 4.425 1.966 1.966 0 0 0-1.84-1.275.983.983 0 0 1-.97-.822l-.073-.437c-.094-.565.25-1.11.8-1.267l.99-.282c.427-.123.783-.418.982-.816l.036-.073a1.453 1.453 0 0 1 2.328-.377L16.5 15h.628a2.25 2.25 0 0 1 1.983 1.186 8.25 8.25 0 0 0-6.345-12.4c.044.262.18.503.389.676l1.068.89c.442.369.535 1.01.216 1.49l-.51.766a2.25 2.25 0 0 1-1.161.886l-.143.048a1.107 1.107 0 0 0-.57 1.664c.369.555.169 1.307-.427 1.605L9 13.125l.423 1.059a.956.956 0 0 1-1.652.928l-.679-.906a1.125 1.125 0 0 0-1.906.172L4.575 15.6Z"
                />
              </svg>
              <span>Osaka Castle</span>
            </p>
            <p>Osaka, Japan</p>
          </Content>
        </ArticleWrapper>
      </Main>
    </>
  );
};

const GlobalStyle = createGlobalStyle`
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
  @import 'normalize.css';

  *,
  *::after,
  *::before {
    box-sizing: border-box;
  }

  :root {
    --x: 0;
    --y: 0;
  }

  html {
    color-scheme: light only;
  }

  body {
    display: flex;
    place-items: center;
    justify-content: center;
    min-height: 100svh;
    touch-action: none;
    font-family: 'SF Pro Text', 'SF Pro Icons', 'AOS Icons', 'Helvetica Neue', Helvetica, Arial, sans-serif, system-ui;
    margin: 0;
    padding: 0.5rem;
  }

  body::before {
    --line: color-mix(in lch, canvasText 25%, transparent);
    --size: 60px;
    content: '';
    height: 100vh;
    width: 100vw;
    position: fixed;
    background: linear-gradient(90deg, var(--line) 1px, transparent 1px var(--size)) 0 -5vmin / var(--size) var(--size),
      linear-gradient(var(--line) 1px, transparent 1px var(--size)) 0 -5vmin / var(--size) var(--size);
    mask: linear-gradient(-15deg, transparent 60%, white);
    top: 0;
    z-index: -1;
  }
`;

const Main = styled.main`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const LinkWrapper = styled.a`
  color: canvasText;
  position: fixed;
  top: 1rem;
  left: 1rem;
  width: 48px;
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  opacity: 0.8;

  :hover,
  :focus-visible {
    opacity: 1;
  }

  .w-9 {
    width: 75%;
  }
`;

const ArticleWrapper = styled.article`
  width: 600px;
  aspect-ratio: 2 / 1.1;
  max-height: calc(100svh - 2rem);
  position: relative;
  overflow: hidden;
  max-width: calc(100% - 2rem);

  @media (orientation: portrait) {
    min-height: 330px;
  }
`;

const Assets = styled.div`
  position: absolute;
  inset: 0;
  border-radius: 4em;
  overflow: hidden;

  img {
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%) scale(1.1); // Zoom in the background images
    height: 100%;
    width: 660px;
    object-fit: cover;
    object-position: center 43%;
    user-select: none;
    pointer-events: none;

    &:first-of-type {
      filter: saturate(1.5) brightness(0.9);
      object-position: calc(-50% + (var(--x) * 10px)) calc(43% + (var(--y) * -10px)); // Adjusted translation
    }

    &:last-of-type {
      object-position: calc(-50% + (var(--x) * 15px)) calc(43% + (var(--y) * -15px)); // Adjusted translation
    }
  }

  h3 {
    position: absolute;
    left: 50%;
    top: 6%;
    margin: 0;
    font-size: 8rem;
    transform: translateX(-50%);
    text-transform: uppercase;
    font-family: 'Bebas Neue', sans-serif;
    color: white;
    transform: translate(calc(-50% + (var(--x) * -10px)), calc(var(--y) * -10px)); // Adjusted translation
  }
`;

const Blur = styled.div`
  --layers: 5;
  position: absolute;
  inset: 0;

  .layer {
    --blur: calc(sin(((var(--layers) - var(--index)) / var(--layers)) * 90deg) * 30);
    --stop: calc(sin(((var(--index)) / var(--layers)) * 90deg) * 15);
    position: absolute;
    inset: 0;
    background: hsl(0 0% 60% / 0.05);
    backdrop-filter: blur(calc(var(--blur) * 1px));
    mask: radial-gradient(150% 130% at 45% 90%, #fff 15%, #0000 calc((15 + var(--stop)) * 1%));
  }
`;

const Content = styled.div`
  min-height: 32%;
  position: absolute;
  bottom: 0;
  width: 100%;
  color: white;
  display: grid;
  gap: 0.2rem;
  place-items: center;
  align-content: center;
  padding-bottom: 0.5rem;
  z-index: 2;

  svg {
    width: 20px;
  }

  p {
    margin: 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.2rem;
    position: relative;

    &:first-of-type::after {
      content: '';
      position: absolute;
      bottom: calc(100% + 1rem);
      left: 50%;
      width: 6ch;
      background: white;
      height: 1px;
      transform: translateX(-50%);
    }

    &:last-of-type {
      opacity: 0.8;
    }
  }
`;

export default GsapComponent;
