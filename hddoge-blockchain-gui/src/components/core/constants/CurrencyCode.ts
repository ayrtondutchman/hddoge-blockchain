import Unit from './Unit';
import { IS_MAINNET } from './constants';

export default {
  [Unit.HDDOGE]: IS_MAINNET ? 'XCH' : 'TXCH',
};
