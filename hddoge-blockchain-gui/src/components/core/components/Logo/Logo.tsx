import React from 'react';
import styled from 'styled-components';
import { Box, BoxProps } from '@material-ui/core';
import { Hddoge } from '@hddoge/icons';

const StyledHddoge = styled(Hddoge)`
  max-width: 100%;
  width: auto;
  height: auto;
`;

export default function Logo(props: BoxProps) {
  return (
    <Box {...props}>
      <StyledHddoge />
    </Box>
  );
}
