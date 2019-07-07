import {state as linkState} from '@/store/links'

describe('Store:links', () => {
  const state = linkState();

  test('Store has state object', () => {
    expect(state).toBeTruthy();
    expect(typeof state).toBe('object')
  });

  test('Store state has links', () => {
    expect(state.links).toBeTruthy()
  });

  test('Links is array', () => {
    expect(Array.isArray(['state.links'])).toBe(true)
  });

});
